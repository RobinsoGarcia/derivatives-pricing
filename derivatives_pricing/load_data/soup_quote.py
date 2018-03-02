from bs4 import BeautifulSoup
import urllib
import re

def get_quote(symbol):
    r = urllib.request.urlopen('https://ca.finance.yahoo.com/quote/'+symbol+'?p='+symbol).read()
    soup = BeautifulSoup(r,"html.parser")
    soup.prettify()

    '''
    Visualize html
    from IPython.display import HTML #another module called IMAGE shows images form the web
    HTML('https://ca.finance.yahoo.com/quote/AAPL?p=AAPL')
    Web Scraping
    http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html
    '''

    table = soup.findAll('table')

    results ={}
    for i in table:
        labels = i.findAll(class_='C(black) W(51%)')
        values = i.findAll(class_='Ta(end) Fw(b) Lh(14px)')
        data = [(x.get_text(),re.sub(',','',y.get_text())) for x,y in zip(labels,values)]
        results.update(dict(data))

    return float(results['Previous Close']),float(results['Beta']),results
