# Asset Allocation
Asset Allocation Simulation with AGG &amp; VTI

## Goal:

The Python script, hw.py, simulates the porfolio construction and management process with the given weights for two ETFs, AGG and VTI, and historical data from yahoo finance. <br />

For the weight of each ETF, any value from 0.1 to 0.9 differing by 0.1 is tested, the rest percentage is used by the other ETF.

Four investment time horizons are considered: 1 year, 3 years, 5 years, and 10 years. The end date for all periods is 2020-12-30. <br />
After analysing the daily record generated, one portfolio strategy would be recommended for each time horizon. <br />

## Analysis:

One year:

| strategy           | rebalancing count | annual return | annual std dev | sharpe ratio | VaR    | annual return chg | std dev chg | annual return chg/std dev chg |
|--------------------|-------------------|---------------|----------------|--------------|--------|-------------------|-------------|-------------------------------|
| 0.1_AGG_0.9_VTI_1y | 0                 | 18.36%        | 30.50%         | 0.5364       | -2.74% |                   |             |                               |
| 0.2_AGG_0.8_VTI_1y | 2                 | 19.25%        | 27.60%         | 0.6251       | -2.54% | 0.89%             | 2.90%       | 0.3068                        |
| 0.3_AGG_0.7_VTI_1y | 2                 | 17.54%        | 24.48%         | 0.6349       | -2.18% | -1.71%            | 3.13%       | -0.5480                       |
| 0.4_AGG_0.6_VTI_1y | 2                 | 15.99%        | 21.28%         | 0.6571       | -1.81% | -1.55%            | 3.19%       | -0.4871                       |
| 0.5_AGG_0.5_VTI_1y | 2                 | 14.74%        | 18.22%         | 0.6992       | -1.46% | -1.25%            | 3.07%       | -0.4071                       |
| 0.6_AGG_0.4_VTI_1y | 2                 | 13.43%        | 15.28%         | 0.7475       | -1.13% | -1.31%            | 2.93%       | -0.4476                       |
| 0.7_AGG_0.3_VTI_1y | 2                 | 12.39%        | 12.56%         | 0.8267       | -0.87% | -1.04%            | 2.72%       | -0.3815                       |
| 0.8_AGG_0.2_VTI_1y | 2                 | 11.99%        | 10.32%         | 0.9676       | -0.64% | -0.40%            | 2.24%       | -0.1782                       |
| 0.9_AGG_0.1_VTI_1y | 0                 | 8.37%         | 8.64%          | 0.7377       | -0.40% | -3.62%            | 1.68%       | -2.1465                       |

* 1-year comparison: (AGG, 7.43%), (VTI, 18.88%), (SPY, 18.4%)
* For 0.1_AGG_0.9_VTI_1y, the portfolio holds 10% AGG and 90% VIT for 1 year.
* The method, conclusion, of the class, portfolio, is used for all calculation. 

Recommend 50-50 for one year:

## Usage:
The historical price data generation code for ETFs is in data.py. You can use the existing data, price.csv, and import into hw.py. <br />

For the main script, hw.py, you can modify following inputs to construct or manage the portfolio differently:
1. initial_bal: initial cash balance to invest
2. end_date: the ending date, a string with 'yyyymmdd' format.
3. start_lst: a list of given starting dates, each is a string with 'yyyymmdd' format.
4. period_lst: a list of numbers matching the given start dates. Each represents the time horizon in year. 
5. rebalancing_trigger: if the weight is off by more than rebalancing_trigger, the portfolio will be rebalanced. 5% is currently used. <br />
Reference: https://investornews.vanguard/rebalancing/#:~:text=Check%20your%20portfolio%20at%20least,meet%20your%20long%2Dterm%20goals.
6. alpha: By modifying alpha, VaR can be changed. Please provide a number from (-1, 1). Recommend 0.05, 0.01.
7. Please read the code carefully if you want to modifying the underlying asset or the portfolio weights, or you can contact me!

## Environment:
Python 3.8.2
Please check requirements.txt to install libraries needed. 
(Command may be needed: pip install -r /path/to/requirements.txt)



