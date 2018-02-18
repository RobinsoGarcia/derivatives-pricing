import quandl
import datetime
#https://chrisconlan.com/download-historical-stock-data-google-r-python/

quandl.ApiConfig.api_key = 'use your key'

def get_quotes(symbol, start_date=(2000, 1, 1), end_date=None):
    """
    symbol is a string representing a stock symbol, e.g. 'AAPL'

    start_date and end_date are tuples of integers representing the year, month,
    and day

    end_date defaults to the current date when None
    """
    if quandl.ApiConfig.api_key == 'use your key':
        quandl.ApiConfig.api_key = input("enter here your quandl API key or go get one @ (https://www.quandl.com/tools/api)")

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
