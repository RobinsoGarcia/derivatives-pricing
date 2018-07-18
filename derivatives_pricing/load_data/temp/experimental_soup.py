import  requests
from bs4 import BeautifulSoup
import re
from json import loads

symbol = 'AAPL'
http = 'https://ca.finance.yahoo.com/quote/'+symbol+'?p='+symbol
soup = BeautifulSoup(requests.get(http).content,"lxml")
script = soup.find("script",text=re.compile("root.App.main")).text
data = loads(re.search("root.App.main\s+=\s+(\{.*\})", script).group(1))
print(data)

stores = data["context"]["dispatcher"]["stores"]

from  pprint import pprint as pp
stores['QuoteSummaryStore']['financialData']['currentPrice']['fmt']

#https://stackoverflow.com/questions/39631386/how-to-understand-this-raw-html-of-yahoo-finance-when-retrieving-data-using-pyt
