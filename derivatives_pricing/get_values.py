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

            c = dv.call(securities[x][0],securities[x][1],securities[x][2],type_=securities[x][4])
            c.N = N
            c.n = n
            v,r = c.price()
            value.append(v)
            error.append(r)
            stds.append(c.std)
            rf.append(c.rf)
            price.append(c.S0)
            #plt.title(str(securities[x]))
            #plt.plot(c.t,c.s[1:])
            #plt.show()

        elif securities[x][3]=='put':

            p = dv.put(securities[x][0],securities[x][1],securities[x][2],type_=securities[x][4])
            p.N = N
            p.n = n
            v,r = p.price()
            value.append(v)
            error.append(r)
            stds.append(p.std)
            rf.append(p.rf)
            price.append(p.S0)
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
