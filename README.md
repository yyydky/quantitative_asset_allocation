# Asset Allocation
Asset Allocation Simulation with AGG &amp; VTI

## Goal:

The Python script, hw.py, simulates the porfolio construction and management process with the given weights for two ETFs, AGG and VTI, and historical data from yahoo finance. <br />

For the weight of each ETF, any value from 0.1 to 0.9 differing by 0.1 is tested, the rest percentage is used by the other ETF.

Four investment time horizons are considered: 1 year, 3 years, 5 years, and 10 years. The end date for all periods is 2020-12-30. <br />
After analysing the daily record generated, one portfolio strategy would be recommended for each time horizon. <br />

## Usage:
The historical price data generation code for ETFs is in data.py. You can use the existing data, price.csv, and import into hw.py. <br />

For the main script, hw.py, you can modify following inputs to construct or manage the portfolio differently:
1. initial_bal: initial cash balance to invest
2. end_date: the ending date, a string with 'yyyymmdd' format.
3. start_lst: a list of given starting dates, each is a string with 'yyyymmdd' format.
4. period_lst: a list of numbers matching the given start dates. Each represents the time horizon in year. 
5. rebalancing_trigger: if the weight is off by more than rebalancing_trigger, the portfolio will be rebalanced. 5% is currently used. 
Reference: https://investornews.vanguard/rebalancing/#:~:text=Check%20your%20portfolio%20at%20least,meet%20your%20long%2Dterm%20goals.
6. By modifying alpha, VaR can be changed. Please provide a number from (-1, 1). Recommend 0.05, 0.01.
7. Please read the code carefully if you want to modifying the underlying asset or the portfolio weights, or contact me!

## Environment:
Python 3.8.2
Please check requirements.txt to install libraries needed. 
(Command may be needed: pip install -r /path/to/requirements.txt)



