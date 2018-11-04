from SimpleBacktester import *

# Isolate the returns of your strategy
returns = portfolio['returns']

# annualized Sharpe ratio
sharp_ratio = np.sqrt(252) * (returns.mean() / returns.std())

print(sharp_ratio)

# Define a trailing 252 trading day window
window = 252
# Calculate the max drawdown in the past window days for each day
rolling_max = aapl['Adj Close'].rolling(window, min_periods=1).max()
daily_drawdown = aapl['Adj Close'] / rolling_max - 1.0

# Calculate the minimum (negative) daily drawdown
max_daily_drawdown = daily_drawdown.rolling(window, min_periods=1).min()

# Plot the results
daily_drawdown.plot(color='b')
max_daily_drawdown.plot()

plt.show()

# Get the number of days in `aapl`

days = (aapl.index[-1] - aapl.index[0]).days

# Calculate the CAGR
cagr = ((((aapl['Adj Close'][-1]) / aapl[' Adj Close'][1])) ** (365.0 / days)) - 1
print(cagr)
