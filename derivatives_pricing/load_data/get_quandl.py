
import quandl
import datetime
import numpy as np

quandl.ApiConfig.api_key = 'API key'

def get_from_quandl(symbol, start_date=(2000, 1, 1), end_date=None):
    """
    symbol is a string representing a stock symbol, e.g. 'AAPL'

    start_date and end_date are tuples of integers representing the year, month,
    and day

    end_date defaults to the current date when None
    """
    query_list = ['WIKI' + '/' + symbol + '.' + str(k) for k in range(1, 13)]

    start_date = datetime.date(*start_date)

    if end_date:
        end_date = datetime.date(*end_date)
    else:
        end_date = datetime.date.today()
        
    return quandl.get(query_list,
            returns='pandas',
            start_date=start_date,
            end_date=end_date,
            collapse='daily',
            order='asc'
            )

def get_quotes(symbol, start_date, end_date=None):

    data = get_from_quandl(symbol, start_date, end_date=None)
    close = [x for x in data.columns if 'Close' in x][0]
    returns = data[close].shift(1)/data[close]-1
    vol = np.std(returns)
    return data[close],returns,vol
