import pandas as pd
import pandas_datareader as pdr
import datetime

aapl = pdr.get_data_yahoo('AAPL', start=datetime.datetime(2006, 10, 1), end=datetime.datetime(2012, 1, 1))

# Return first rows of `aapl`
aapl.head()

# Return last rows of `aapl`
aapl.tail()

# Describe `aapl`
aapl.describe()

aapl.to_csv('aapl_ohlc.csv')
df = pd.read_csv('aapl_ohlc.csv', header=0, index_col='Date', parse_dates=True)

# Inspect the index
aapl.index

# Inspect the columns
aapl.columns

# Select only the last 10 observations of `Close`
ts = aapl['Close'][-10:]

# Check the type of `ts`
type(ts)

# Inspect the first rows of November-December 2006
print(aapl.loc[pd.Timestamp('2006-11-01'):pd.Timestamp('2006-12-31')].head())

# Inspect the first rows of 2007
print(aapl.loc['2007'].head())

# Inspect November 2006
print(aapl.iloc[22:43])

# Inspect the 'Open' and 'Close' values at 2006-11-01 and 2006-12-01
print(aapl.iloc[[22, 43], [0, 3]])

# Sample 20 rows
sample = aapl.sample(20)

# Print `sample`
print(sample)

# Resample to monthly level
monthly_aapl = aapl.resample('M').mean()

# Print `monthly_aapl`
print(monthly_aapl)

aapl.asfreq("M", method='fill')

aapl['diff'] = aapl.Open - aapl.Close

del aapl['diff']

import matplotlib.pyplot as plt

# Data visualization
aapl['Close'].plot(grid=True, color='red')
plt.show()

import numpy as np

daily_close = aapl[['Adj Close']]

# daily return
daily_pct_change = daily_close.pct_change()

# Replace NA values with 0
daily_pct_change.fillna(0, inplace=True)

# Inspect daily return
print(daily_pct_change)

# Daily log returns
daily_log_returns = np.log(daily_close.pct_change() + 1)
print(daily_log_returns)



# Resample `aapl` to business months, take last observation as value
monthly = aapl.resample('BM').apply(lambda x: x[-1])

# Calculate the monthly percentage change
monthly.pct_change()

# Resample `aapl` to quarters, take the mean as value per quarter
quarter = aapl.resample("4M").mean()

# Calculate the quarterly percentage change
quarter.pct_change()
