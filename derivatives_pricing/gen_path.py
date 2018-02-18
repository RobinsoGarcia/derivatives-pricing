import derivatives_pricing.load_data.quandl as quandl
import derivatives_pricing.load_data.soup_quote as soup
import derivatives_pricing.load_data.rf as rate
import derivatives_pricing.sim.wiener as wiener
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

symbol = 'AAPL'
start = (2015,1,1)

p,beta,_ = soup.get_quote(symbols)

rf = rate.get_rate()

stock_hist,returns,vol = quandl.get_quotes(symbol, start_date=start, end_date=None)

mean_price,results = wiener.get_path(p,vol,rf,1,500,1)

plt.plot(mean_price)
