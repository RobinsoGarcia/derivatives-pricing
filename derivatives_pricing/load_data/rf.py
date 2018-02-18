from bs4 import BeautifulSoup
import urllib
import re


'''
rates from FRED's economic data
'''
def get_rate(rate='OvernightUSD'):
    rates = {'3mth-Tbill':'TB3MS',
    '1yr-Tbill':'TB1YR',
    '10yr-Treasury':'DGS10',
    '3mth-LiborUSD':'USD3MTD156N',
    '12mth-LiborUSD':'USD12MD156N',
    'OvernightUSD':'USDONTD156N'}

    rate = rates[rate]
    r = urllib.request.urlopen('https://fred.stlouisfed.org/series/'+rate).read()
    soup = BeautifulSoup(r,"html.parser")
    soup.prettify()
    x = soup.findAll(class_='series-meta-observation-value')
    rf = float(x[0].get_text())
    return rf/100
