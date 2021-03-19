import csv
from datetime import date
import logging
import math
import pandas as pd

#constants
# initial cash balance to invest
initial_bal = 1000000
# Change VaR with modifying alpha. Please provide a number from (-1, 1). Recommend 0.05, 0.01.
alpha = 0.05

class portfolio:

    def __init__(self, period, weight):
        self.AGG_weight = weight
        self.VTI_weight = round(1 - weight, 1)
        self.cash_balance = 1000000
        self.curr_shares = {
            'AGG': 0,
            'VTI': 0
        }
        # if the weight is off by more than rebalancing_trigger, the portfolio will be rebalanced
        self.rebalancing_trigger = 0.05
        self.rebalancing_count = 0
        self.daily_balance_header = ['date', 'total', 'AGG_price', 'VTI_price',
                                     'AGG_shares', 'VTI_shares', 'AGG_pct', 'VTI_pct',
                                     'AGG_chg', 'VTI_chg', 'cash', 'rebalance']
        self.daily_balance = [self.daily_balance_header]
        self.period = period

    # to calculate daily portfolio balance and rebalance the portfolio if needed
    def daily_record(self, data):
        price_AGG = data['AGG_adjclose']
        price_VTI = data['VTI_adjclose']

        AGG_bal = self.curr_shares['AGG'] * price_AGG
        VTI_bal = self.curr_shares['VTI'] * price_VTI

        shares_sum = AGG_bal + VTI_bal + self.cash_balance

        AGG_pct = AGG_bal / shares_sum
        VTI_pct = VTI_bal / shares_sum

        AGG_chg = 0
        VTI_chg = 0

        #rebalance portfolio if the weight is off more than 5%
        # sell AGG buy VTI
        if ((AGG_pct - self.AGG_weight) >= self.rebalancing_trigger):
            self.rebalancing_count += 1
            AGG_chg = -1 * abs(self.curr_shares['AGG'] - int(math.floor(shares_sum * self.AGG_weight / price_AGG)))
            self.cash_balance += AGG_chg * price_AGG * (-1)
            VTI_chg = int(math.floor(self.cash_balance / price_VTI))
            self.cash_balance += VTI_chg * price_VTI * (-1)

        # sell VTI buy AGG
        elif((VTI_pct - self.VTI_weight) >= self.rebalancing_trigger):
            self.rebalancing_count += 1
            VTI_chg = -1 * abs(self.curr_shares['VTI'] - int(math.floor(shares_sum * self.VTI_weight / price_VTI)))
            self.cash_balance += VTI_chg * price_VTI * (-1)
            AGG_chg = int(math.floor(self.cash_balance / price_AGG))
            self.cash_balance += AGG_chg * price_AGG * (-1)

        else:
            pass

        #format the daily record
        self.curr_shares['AGG'] += AGG_chg
        self.curr_shares['VTI'] += VTI_chg
        lst = [data['date'], shares_sum, price_AGG, price_VTI,
               self.curr_shares['AGG'], self.curr_shares['VTI'],
               AGG_bal / shares_sum, VTI_bal / shares_sum,
               AGG_chg, VTI_chg,
               self.cash_balance, self.rebalancing_count]
        self.daily_balance.append(lst)

    # generate first day record
    def initialize(self, data):
        fund_AGG = self.AGG_weight * self.cash_balance
        fund_VTI = self.VTI_weight * self.cash_balance
        price_AGG = data['AGG_adjclose']
        price_VTI = data['VTI_adjclose']

        self.curr_shares['AGG'] = int(math.floor(fund_AGG / price_AGG))
        self.curr_shares['VTI'] = int(math.floor(fund_VTI / price_VTI))
        AGG_bal = self.curr_shares['AGG'] * price_AGG
        VTI_bal = self.curr_shares['VTI'] * price_VTI

        total = self.cash_balance
        self.cash_balance = self.cash_balance - AGG_bal - VTI_bal
        shares_sum = AGG_bal + VTI_bal

        lst = [data['date'], total, price_AGG, price_VTI,
               self.curr_shares['AGG'], self.curr_shares['VTI'],
               AGG_bal/shares_sum, VTI_bal/shares_sum,
               self.curr_shares['AGG'], self.curr_shares['VTI'],
               self.cash_balance, self.rebalancing_count]
        self.daily_balance.append(lst)

    # export every day record to csv for verifying
    def export_record(self):
        bal_filename = str(self.AGG_weight) + "_AGG_" + str(self.VTI_weight) + "_VTI_record_" + str(self.period) + "y.csv"

        with open(bal_filename, 'w') as f:
            write = csv.writer(f)
            write.writerows(self.daily_balance)
        logging.debug("Done: " + bal_filename)

    # table for strategy overview
    def conclusion(self):
        df = pd.DataFrame(self.daily_balance)
        new_header = df.iloc[0]
        df = df[1:]
        df.columns = new_header
        df['pct_chg'] = df['total'].pct_change()
        df = df.iloc[1:]

        # std dev
        annualized_std = df['pct_chg'].std() * math.sqrt(252)

        # VaR
        sorted_return = df['pct_chg'].sort_values(ascending=True)
        var = sorted_return.quantile(q=alpha, interpolation='higher')

        # daily return => annual return; considering the return size, exclude MER for now
        df['pct_chg'] = df['pct_chg'].apply(lambda a: a + 1)
        annualized_compound_daily_return = pow(df['pct_chg'].product(), (1 / len(df['pct_chg']))) - 1
        annual_return = pow((1 + annualized_compound_daily_return), 252) - 1

        # sharpe ratio， risk free rate: 2%
        sharpe = (annual_return - 0.02) / annualized_std

        # row name
        portfolio_overview = str(self.AGG_weight) + "_AGG_" + str(self.VTI_weight) + "_VTI_" + str(self.period) + "y"

        lst = [portfolio_overview, self.rebalancing_count, '{:.4%}'.format(annual_return),
               '{:.4%}'.format(annualized_std), '{:.4f}'.format(sharpe), '{:.4%}'.format(var)]
        df.to_csv(portfolio_overview+'_check.csv')
        return lst

if __name__ == "__main__":
    today_date = date.today().strftime("%Y%m%d")
    logging.basicConfig(filename=today_date + '.log',
                        format='%(levelname)s %(asctime)s :: %(message)s',
                        filemode='w',
                        level=logging.DEBUG)

    # the ending date, a string with 'yyyymmdd' format.
    end_date = '20201230'

    # a list of given starting dates
    start_lst = ['20200102', '20180102', '20160102', '20110102']

    # a list of numbers matching the given start dates
    period_lst = [1, 3, 5, 10]

    # import historical data
    raw_data = pd.read_csv('price.csv')
    raw_data['date'] = raw_data['date'].apply(str)

    lst_portfolio = []
    final_result_table = [['strategy', 'rebalancing count', 'annual return', 'annual std dev', 'sharpe ratio', 'VaR']]

    for x in range (4):
        # generate dataframe with given time horizon
        start_date = start_lst[x]
        period = period_lst[x]
        price_df = raw_data.loc[(raw_data['date'] >= start_date) & (raw_data['date'] <= end_date)]

        # generate 9 strategies from (0.1, 0.9) to (0.9, 0.1)
        for weight in range(1, 10):
            AGG_weight = round(weight / 10, 1)
            lst_portfolio.append(portfolio(period, AGG_weight))
            curr_port = lst_portfolio[-1]
            curr_port.initialize(price_df.iloc[0])

        for index, row in price_df[1:].iterrows():
            for portfolio in lst_portfolio:
                portfolio.daily_record(row)

        # to manually verify calculation and data
        for portfolio in lst_portfolio:
            # portfolio.export_record()
            final_result_table.append(portfolio.conclusion())
        final_result = pd.DataFrame(final_result_table)
        final_result.to_csv(str(period) + 'y_final.csv')
















