import derivatives_pricing.sim.gen_path as gp
from derivatives_pricing.securities import derivatives as dv
import derivatives_pricing.sim.wiener as wiener

import derivatives_pricing.load_data.quandl as quandl
import derivatives_pricing.load_data.soup_quote as soup
import derivatives_pricing.load_data.rf as rate
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from datetime import datetime
import pandas as pd
td = datetime.today()

start = np.busday_offset(td,-252*5,roll="modifiedpreceding").astype(datetime)

class derivative():
    def __init__(self,symbol,strike,maturity,type_='european',check_BS=1):
        self.symbol = symbol
        self.K = strike
        self.type_ = type_
        self.T = int(np.busday_count(datetime.today(), pd.Timestamp(maturity)))/252
        self.check_BS = check_BS
        self.std_horiz = 3
        self.get_current_data()
        self.init_data()
        self.N = 500
        self.n = 300



    def build_path(self):
        self.series,self.time,self.results = wiener.get_path(S0=self.S0,vol=self.std,rf=self.rf,T=self.T,N=self.N,n=self.n)
        self.value = np.mean(self.f(self.results),axis=1)
        print(self.value[-1])
        dc = np.exp(-1*self.rf*self.time)
        self.pv = np.multiply(dc,self.value[1:])
        pass

    def get_current_data(self,gm=1):
        #S,beta,_ = soup.get_quote(self.symbol)
        rf = rate.get_rate()
        start = np.busday_offset(td,-252*self.std_horiz,roll="modifiedpreceding").astype(datetime)
        start = (start.year,start.month,start.day)
        stock_hist,returns,std = quandl.get_quotes(self.symbol,start_date=start,end_date=None)
        std = std*np.sqrt(252)
        if gm==1:
             x = (pd.Series(returns)-pd.Series(returns).mean())
             w =  1/(1+x**2)**2
             returns = returns*w
             std = np.std(returns)*np.sqrt(252)

        print("Summary of past returns for "+self.symbol)
        print(pd.Series(returns).describe())
        print('std: {}'.format(std))
        print('stock price: {}'.format(stock_hist[-1]))
        self.std = std
        self.S0 = stock_hist[-1]
        #self.beta = beta
        self.rf = rf
        pass

    def price(self,std=0):
        if std!=0:
            self.std=std

        if self.type_ == 'european':
            v0 = 0
            n=100
            count = 0
            _,_,results= wiener.get_path(S0=self.S0,vol=self.std,rf=self.rf,T=self.T,N=1,n=n)
            v1 = np.mean(self.f(results[-1]))*np.exp(-self.T*self.rf) #at present value
            while np.abs(v1-v0) > 0.001:
                v0 = v1
                _,_,results= wiener.get_path(S0=self.S0,vol=self.std,rf=self.rf,T=self.T,N=1,n=n)
                v1 = np.mean(self.f(results[-1]))*np.exp(-self.T*self.rf) #at present value
                n *= 10
                count += 1
                print("iteration:",count,":",v1)
                if count > 5:
                    break
            v=v1
            if self.check_BS==1:
                BS_value = BS(S=self.S0,K=self.K,r=self.rf,
                std=self.std,t=self.T,option_type=self.option_type1)
                error = v - BS_value
                print('MC result: {}'.format(v))
                print('BS minus MC = {}'.format(error))
        if self.type_ == 'american':
            v = np.max(self.pv)
            error = 'nan'
        return v,error

class call(derivative):
    def init_data(self):
        self.option_type1 = 'call'
        self.check_BS = 1
        print('Type of derivative: {}'.format(self.option_type1))
        pass

    def f(self,S):
        return np.maximum(S-self.K,0)

class put(derivative):
    def init_data(self):
        self.option_type1 = 'put'
        print('Type of derivative: {}'.format(self.option_type1))

    def f(self,S):
        return np.maximum(self.K-S,0)

def BS(S,K,r,std,t,option_type):
    d1 = (np.log(S/K)+(r+std/2)*t)/(std*np.sqrt(t))
    d2 = d1-std*np.sqrt(t)
    if option_type=='call':
        N1 = norm.cdf(d1)
        N2 = norm.cdf(d2)
        c = S*N1-N2*K*np.exp(-r*t)
        print('call_BS: {}'.format(c))
        return c
    elif option_type=='put':
        N1 = norm.cdf(-d1)
        N2 = norm.cdf(-d2)
        p = -S*N1+N2*K*np.exp(-r*t)
        print('put_BS: {}'.format(p))
        return p
