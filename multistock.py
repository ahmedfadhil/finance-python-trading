from main import *
def get(tickers, startdate, enddate):
    def data(ticker):
        return (pdr.get_data_yahoo())