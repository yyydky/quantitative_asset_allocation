import pandas as pd
from yahoofinancials import YahooFinancials

# generate data for AGG
AGG = YahooFinancials('AGG')
data_AGG = AGG.get_historical_price_data(start_date='2004-01-02',
                                         end_date='2020-12-31',
                                         time_interval='daily')
AGG_df = pd.DataFrame(data_AGG['AGG']['prices'])
AGG_df = AGG_df.drop('date', axis=1).set_index('formatted_date')
AGG_df.index = pd.to_datetime(AGG_df.index)
AGG_df.head(10)
AGG_df = AGG_df.rename(columns={'adjclose': 'AGG_adjclose'})

# generate data for VTI
VTI = YahooFinancials('VTI')
data_VTI = VTI.get_historical_price_data(start_date='2004-01-02',
                                         end_date='2020-12-31',
                                         time_interval='daily')
VTI_df = pd.DataFrame(data_VTI['VTI']['prices'])
VTI_df = VTI_df.drop('date', axis=1).set_index('formatted_date')
VTI_df.index = pd.to_datetime(VTI_df.index)
VTI_df = VTI_df.rename(columns={'adjclose': 'VTI_adjclose'})

# merge data and export
price_df = VTI_df[['VTI_adjclose']].merge(AGG_df[['AGG_adjclose']],
                                          on = 'formatted_date',how = 'inner')
idx = price_df.index
price_df.reset_index(drop=True, inplace=True)
price_df.insert(0, 'date', idx)
price_df['date'] = price_df['date'].dt.strftime('%Y%m%d')
price_df.to_csv('price.csv')
