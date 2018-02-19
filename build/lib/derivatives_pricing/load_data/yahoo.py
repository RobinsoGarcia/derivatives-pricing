import pandas_datareader as pr
from pandas_datareader import data
from yahoo_finance import Share

def get_quote(ticker):
    print('not working...')
    '''
    yahoo = Share(ticker)
    close = yahoo.get_price()
    date = yahoo.get_trade_datetime()
    print('Price: {}'.format(close))
    print('from {}'.format(date))
    '''
    pass

def data_reader(stocks,start_date,end_date):
    #http://www.learndatasci.com/python-finance-part-yahoo-finance-api-pandas-matplotlib/

    # Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
    tickers = stocks

    # Define which online source one should use
    data_source = 'yahoo'

    # We would like all available data from 01/01/2000 until 12/31/2016.
    start_date = start_date
    end_date = end_date

    # User pandas_reader.data.DataReader to load the desired data. As simple as that.
    panel_data = data.DataReader(tickers, data_source, start_date, end_date)
    data_ = panel_data.loc['Close'].sort_index(ascending=True)

    returns = data_.shift(1)/data_-1

    data_.to_csv('yahoo-fin-data.csv')

    print("data description:\n\nmeans: \n{}\n\nstds: \n{}".format(data_.mean(),data_.std()))
    print("data description:\n\nmax: \n{}\n\nmin: \n{}".format(data_.max(),data_.min()))
    return returns,data_
