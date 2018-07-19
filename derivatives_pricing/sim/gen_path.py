import derivatives_pricing.load_data.get_quandl as gq
import derivatives_pricing.load_data.soup_quote as soup
import derivatives_pricing.load_data.rf as rate
import derivatives_pricing.sim.wiener as wiener
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
td = datetime.today()
#datetime.utcfromtimestamp(start_date)
#start_date.astype(datetime)
#np.busday_count(datetime.today(), of)

def gen_path(symbol,start,end=None,vol=0,T=1,N=800,n=100):
    print('Number of time steps: {}'.format(N))
    print('Number of simulations: {}'.format(n))
    S,beta,_ = soup.get_quote(symbol)

    rf = rate.get_rate()

    if vol==0:
        start = np.busday_offset(td,-252*2,roll="modifiedpreceding").astype(datetime)
        print("volatility: std of the stock returns for the past two years")
        start = (start.year,start.month,start.day)
        stock_hist,returns,std = gq.get_quotes(symbol,start_date=start,end_date=None)
    print('daily std: {}'.format(std))

    std = std*np.sqrt(252)

    mean_price,t,results = wiener.get_path(S0=S,vol=std,rf=rf,T=T,N=N,n=n)

    plt.title('Average path')
    plt.plot(t,mean_price[1:])
    plt.show()
    return mean_price,t,rf,std,results
