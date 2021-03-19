# Asset Allocation
Asset Allocation Simulation with AGG &amp; VTI

## Goal:

The Python script, main.py, simulates the porfolio construction and management process with the given weights for two ETFs, AGG and VTI using historical price data from Yahoo Finance. <br />

Four investment time horizons are considered: 1 year, 3 years, 5 years, and 10 years. The ending date for all periods is 2020-12-30. <br />

After analysing the daily record generated, one portfolio strategy would be recommended for each time horizon. <br />

## Analysis:

**One year:**
| strategy           | rebalancing count | annual return | annual std dev | sharpe ratio | VaR    |
|--------------------|-------------------|---------------|----------------|--------------|--------|
| 0.1_AGG_0.9_VTI_1y | 0                 | 18.36%        | 30.50%         | 0.5364       | -2.74% |
| 0.2_AGG_0.8_VTI_1y | 2                 | 19.25%        | 27.60%         | 0.6251       | -2.54% |
| 0.3_AGG_0.7_VTI_1y | 2                 | 17.54%        | 24.48%         | 0.6349       | -2.18% |
| 0.4_AGG_0.6_VTI_1y | 2                 | 15.99%        | 21.28%         | 0.6571       | -1.81% |
| 0.5_AGG_0.5_VTI_1y | 2                 | 14.74%        | 18.22%         | 0.6992       | -1.46% |
| 0.6_AGG_0.4_VTI_1y | 2                 | 13.43%        | 15.28%         | 0.7475       | -1.13% |
| 0.7_AGG_0.3_VTI_1y | 2                 | 12.39%        | 12.56%         | 0.8267       | -0.87% |
| 0.8_AGG_0.2_VTI_1y | 2                 | 11.99%        | 10.32%         | 0.9676       | -0.64% |
| 0.9_AGG_0.1_VTI_1y | 0                 | 8.37%         | 8.64%          | 0.7377       | -0.40% |

* 1-year return: (AGG, 7.43%), (VTI, 18.88%), (SPY, 18.4%)
* Strategy naming: for example, 0.1_AGG_0.9_VTI_1y is the portfolio that holds 10% AGG and 90% VIT for 1 year.
* Recommend 0.8_AGG_0.2_VTI_1y: <br />
The combination has the highest sharpe ratio and the second best VaR.

**Three years:**
| strategy           | rebalancing count | annual return | annual std dev | sharpe ratio | VaR    |
|--------------------|-------------------|---------------|----------------|--------------|--------|
| 0.1_AGG_0.9_VTI_3y | 0                 | 13.24%        | 20.87%         | 0.5387       | -1.95% |
| 0.2_AGG_0.8_VTI_3y | 0                 | 12.42%        | 18.55%         | 0.5619       | -1.68% |
| 0.3_AGG_0.7_VTI_3y | 3                 | 12.15%        | 16.55%         | 0.6133       | -1.47% |
| 0.4_AGG_0.6_VTI_3y | 3                 | 11.13%        | 14.30%         | 0.6388       | -1.26% |
| 0.5_AGG_0.5_VTI_3y | 3                 | 10.22%        | 12.18%         | 0.6753       | -1.04% |
| 0.6_AGG_0.4_VTI_3y | 3                 | 9.50%         | 10.09%         | 0.7429       | -0.78% |
| 0.7_AGG_0.3_VTI_3y | 3                 | 8.62%         | 8.25%          | 0.8015       | -0.61% |
| 0.8_AGG_0.2_VTI_3y | 0                 | 7.24%         | 6.49%          | 0.8076       | -0.41% |
| 0.9_AGG_0.1_VTI_3y | 0                 | 6.33%         | 5.51%          | 0.7859       | -0.31% |

* 3-year return: (AGG, 5.28%), (VTI, 12.4%), (SPY, 14%)
* Recommend 0.8_AGG_0.2_VTI_3y:  <br />
The combination has the highest sharpe ratio and the second best VaR. 

**Five years:**
| strategy           | rebalancing count | annual return | annual std dev | sharpe ratio | VaR    |
|--------------------|-------------------|---------------|----------------|--------------|--------|
| 0.1_AGG_0.9_VTI_5y | 0                 | 14.78%        | 17.64%         | 0.7243       | -1.59% |
| 0.2_AGG_0.8_VTI_5y | 3                 | 14.05%        | 15.45%         | 0.7798       | -1.37% |
| 0.3_AGG_0.7_VTI_5y | 4                 | 12.78%        | 13.70%         | 0.7874       | -1.19% |
| 0.4_AGG_0.6_VTI_5y | 4                 | 11.63%        | 11.77%         | 0.8179       | -1.01% |
| 0.5_AGG_0.5_VTI_5y | 4                 | 10.44%        | 10.01%         | 0.8431       | -0.83% |
| 0.6_AGG_0.4_VTI_5y | 4                 | 9.31%         | 8.30%          | 0.881        | -0.66% |
| 0.7_AGG_0.3_VTI_5y | 2                 | 7.94%         | 6.71%          | 0.8855       | -0.51% |
| 0.8_AGG_0.2_VTI_5y | 1                 | 6.82%         | 5.31%          | 0.9067       | -0.36% |
| 0.9_AGG_0.1_VTI_5y | 1                 | 5.73%         | 4.72%          | 0.7896       | -0.30% |

* 5-year return: (AGG, 4.38%), (VTI, 13.28%), (SPY, 16.71%)
* Recommend 0.8_AGG_0.2_VTI_5y:  <br />
The combination has the highest sharpe ratio and the second best VaR. 

**Ten years:**
| strategy            | rebalancing count | annual return | annual std dev | sharpe ratio | VaR    |
|---------------------|-------------------|---------------|----------------|--------------|--------|
| 0.1_AGG_0.9_VTI_10y | 1                 | 12.85%        | 15.81%         | 0.6863       | -1.48% |
| 0.2_AGG_0.8_VTI_10y | 4                 | 12.01%        | 14.01%         | 0.7141       | -1.32% |
| 0.3_AGG_0.7_VTI_10y | 7                 | 11.12%        | 12.29%         | 0.7416       | -1.15% |
| 0.4_AGG_0.6_VTI_10y | 8                 | 10.08%        | 10.56%         | 0.7652       | -0.97% |
| 0.5_AGG_0.5_VTI_10y | 8                 | 9.09%         | 8.87%          | 0.7994       | -0.80% |
| 0.6_AGG_0.4_VTI_10y | 8                 | 8.11%         | 7.25%          | 0.8425       | -0.63% |
| 0.7_AGG_0.3_VTI_10y | 6                 | 7.04%         | 5.73%          | 0.8803       | -0.46% |
| 0.8_AGG_0.2_VTI_10y | 3                 | 5.90%         | 4.60%          | 0.8483       | -0.35% |
| 0.9_AGG_0.1_VTI_10y | 1                 | 4.94%         | 3.92%          | 0.7492       | -0.30% |

* 10-year return: (AGG, 3.76%), (VTI, 11.61%), (SPY, 13.31%)
* Recommend 0.7_AGG_0.3_VTI_10y:  <br />
The combination has the highest sharpe ratio and the third best VaR. 

## Usage:
The historical price data generation code for ETFs is in data.py, and the reformatted data is saved in price.csv. The main.py imports data from price.csv. <br />
The main.py is used to create daily portfolio balance record and the final analysis.
The implementation and calculation details can be found in the main.py as comments. 

## Environment:
Python 3.8.2
Please check requirements.txt to install libraries needed. 
(Command: pip install -r /path/to/requirements.txt)



