from mvngavgcrsovr import *
# Get the number of days in `aapl`

days = (aapl.index[-1] - aapl.index[0]).days

# Calculate the CAGR
cagr = ((((aapl['Adj Close'][-1]) / aapl[' Adj Close'][1])) ** (365.0 / days)) - 1
print(cagr)
