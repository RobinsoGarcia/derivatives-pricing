from derivatives_pricing.securities.derivatives import *
from  derivatives_pricing.sim.wiener import *
import matplotlib.pyplot as plt
import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-s","--stock",type=str,help="stock ticker")

    parser.add_argument("-K","--strike",type=int,help="Strike value")

    parser.add_argument("-T","--maturity",help="Maturity date as per YYYY-M-DD | string")

    parser.add_argument("-o","--option_type",help="Option type: 'european' or 'american'")

    parser.add_argument("-N",type=int,help="Number of time divisions for simulating the wiener process, dt",default=1000)

    parser.add_argument("-n",type=int,help="Number of paths generated, number of simulations",default=1000)

    args = parser.parse_args()

    ticker = args.stock
    strike = args.strike
    maturity = args.maturity
    type_ = args.option_type
    print(maturity)
    c = call(ticker,strike,maturity,type_='european',check_BS=1)
    print('Annualized volatility: {}'.format(c.std))
    c.n=args.n
    c.N=args.N
    print(c.n,c.N)
    print('Price {}'.format(c.price()))

    c.build_path()
    plt.title('Average simulaated stock price')
    plt.ylabel('price')
    plt.plot(c.results[:,-100:].T);
