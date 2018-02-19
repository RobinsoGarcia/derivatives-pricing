import derivatives_pricing.sim.gen_path as gp
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from datetime import datetime
td = datetime.today()

class derivative():
    def __init__(self,symbol,strike,maturity,type_='european'):
        self.symbol = symbol
        self.K = strike
        self.T = maturity
        self.type_ = type_

    def price(self,vol=0,N=500,n=100):
        self.s,self.t,self.r,self.std,results = gp.gen_path(symbol=self.symbol,
        start=(td.year,td.month,td.day),end=self.T,vol=vol,N=N,n=n)
        value = np.mean(self.f(results),axis=1)
        dc = np.exp(-1*self.r*self.t)
        self.price_series = np.multiply(dc,value[1:])
        if self.type_ == 'european':
            v = self.price_series[-1]
            if self.check_BS==1:
                BS_value = BS(self.s[0],self.K,self.r,self.std,self.T,option_type=self.option_type1)
                error = v - BS_value
                print('MC result: {}'.format(v))
                print('BS minus MC = {}'.format(error))
        if self.type_ == 'american':
            v = np.max(self.price_series)
            error = 'nan'
        return v,error

class call(derivative):
    def f(self,S):
        self.option_type1 = 'call'
        self.check_BS = 1
        print('Type of derivative: {}'.format(self.option_type1))
        return np.maximum(S-self.K,0)

class put(derivative):
    def f(self,S):
        self.option_type1 = 'put'
        self.check_BS = 1
        print('Type of derivative: {}'.format(self.option_type1))
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
