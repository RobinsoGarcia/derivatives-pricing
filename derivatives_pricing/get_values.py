from derivatives_pricing.securities import derivatives as dv
import matplotlib.pyplot as plt
import pandas as pd
import sys
import json
from datetime import date,time
import numpy as np
t = np.busday_count(date.today(), pd.Timestamp('2018-3-29'))


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    hmdir = str(sys.argv[1])

    f_in = open(hmdir)
    dic = json.load(f_in)

    securities =dic[0]

    simulation_data = dic[1]
    N,n = simulation_data['N'],simulation_data['n']

    value = []
    error = []
    stds = []
    rf = []
    price = []
    for x in securities:
        if securities[x][3]=='call':
            t = np.busday_count(date.today(), pd.Timestamp(securities[x][2]))
            c = dv.call(securities[x][0],securities[x][1],int(t)/252.0,type_=securities[x][4])
            v,r = c.price(N=N,n=n)
            value.append(v)
            error.append(r)
            stds.append(c.std)
            rf.append(c.r)
            price.append(c.s[0])
            #plt.title(str(securities[x]))
            #plt.plot(c.t,c.s[1:])
            #plt.show()

        elif securities[x][3]=='put':
            t = np.busday_count(date.today(), pd.Timestamp(securities[x][2]))
            p = dv.put(securities[x][0],securities[x][1],int(t)/252.0,type_=securities[x][4])
            v,r = p.price(N=N,n=n)
            value.append(v)
            error.append(r)
            stds.append(p.std)
            rf.append(p.r)
            price.append(p.s[0])
            #plt.title(str(securities[x]))
            #plt.plot(p.t,p.s[1:])
            #plt.show()

    data = pd.DataFrame(securities).T
    data.columns = ['Stock','Strike','Maturity','type1','type2']
    data['value'] = value
    data['error'] = error
    data['stds'] = stds
    data['rfs'] = rf
    data['s0'] = price
    print(data.T)

if __name__=="__main__":
    main()
