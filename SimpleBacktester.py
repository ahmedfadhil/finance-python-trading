from main import *
import pandas as pd
import matplotlib.pyplot as plt

from trading_strategy import signals

initial_capital = float(100000.0)

# Create a data frame position
positions = pd.DataFrame(index=signals.index).fillna(0.0)

# Buy 100 shares
positions['AAPL'] = 100 * signals['signals']

# Initialize the portfolio with value owned
portfolio = positions.multiply(aapl['Adj Close'], axis=0)

# Store the difference in shares owned
pos_diff = positions.diff()

# Add `holdings` to portfolio
portfolio['holdings'] = (positions.multiply(aapl['Adj Close'], axis=0)).sum(axis=1)

# Add `cash` to portfolio
portfolio['cash'] = initial_capital - (pos_diff.multiply(aapl['Adj Close'], axis=0)).sum(axis=1).cumsum()

# Add `total` to portfolio
portfolio['total'] = portfolio['cash'] + portfolio['holdings']

# Add `returns` to portfolio
portfolio['returns'] = portfolio['total'].pct_change()

print(portfolio.head())

# plotting the portfolio
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Portfolio value in $')

# Plot the equity curve in dollars
portfolio['total'].plot(ax=ax1, lw=2)
ax1.plot(portfolio.loc[signals.positions == 1].index, portfolio.total[signals.positions == 1], '^', markersize=10,
         color='r')
ax1.plot(portfolio.loc[signals.positions == -1].index, portfolio.total[signals.positions == -1], 'v', markersize=10,
         colo='k')
plt.show()
