# Import `pyplot` module as `plt`
import matplotlib.pyplot as plt
import pandas as pd
from main import *
from multistock import *

show_window = 40
long_window = 100

# Initialize the `signals` DataFrame with the `signal` column
signals = pd.DataFrame(index=aapl.index)
signals['signal'] = 0.0

# Create short simple moving average over the short window
signals['short_mavg'] = aapl['Close'].rolling(window=show_window, min_periods=1, center=False).mean()

# Create long simple moving average over the short window
signals['long_mavg'] = aapl['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][show_window:] = np.where(signals['short_mavg'][show_window:] > signals['long_mavg'][show_window:],
                                           1.0, 0.0)

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# print result
print(signals)

fig = plt.figure()

# Add a subplot and label for y-axis

ax1 = fig.add_subplot(111, ylabel="Price in $")

# Plot the closing price
aapl['Close'].plot(ax=ax1, color='r', lw=2.)

signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

# Plot the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0], '^', markersize=10,
         color='m')

# Plot the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index, signals.short_mavg[signals.positions == -1.0], 'v',
         markersize=10,color='k')

plt.show()
