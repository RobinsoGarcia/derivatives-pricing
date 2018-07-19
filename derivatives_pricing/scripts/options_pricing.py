from derivatives_pricing.sim.wiener import *
import matplotlib.pyplot as plt
from derivatives_pricing.securities.derivatives import *
import argparse
import matplotlib.pyplot as plt


if __name__=="__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-o","--option_type",default="call",help="call or put (default=call)")

    parser.add_argument("-t","--type",default="european",help="Type: european or american")

    parser.add_argument("-T","--maturity",help="Maturity YYYY-MM-DD")

    parser.add_argument("-s","--stock",help="list of stock tickers")

    parser.add_argument("-K","--strike",type=int,help="Strike price (in USD)")

    parser.add_argument("-bs","--BlackScholes",help="True to compare simulation with Black and Scholes formula (european) or False to run simulation only")

    parser.add_argument("-plt","--plot",default='False',help="True to show the brownian path")

    parser.add_argument("-tvol","--std_horiz",type=float,default=3,help="change to define how many years to consider in the calculation of the volatility (default is 3 years)")

    parser.add_argument("-p","--precision",type=float,default=1e-3,help="Set the precision to interrupt the simulation. Check for the price difference on each iteration, ideally, the change should be minimal")

    parser.add_argument("-i","--iterations",type=int,default=5,help="Set the number of iterations, improves the result. The goal is to see little price changes one simulation after the other.")

    args = parser.parse_args()
    ticker = args.stock
    strike = args.strike
    maturity = args.maturity
    type_ = args.type
    if args.BlackScholes == 'False':
        check_BS=0
    else:
        check_BS=1

    if args.option_type=='call':
        o = call(ticker,strike,maturity,type_,check_BS)
    elif args.option_type=='put':
        o = put(ticker,strike,maturity,type_,check_BS)

    o.std_horiz=args.std_horiz
    o.precision = args.precision
    o.iter = args.iterations
    print('Annualized volatility: {}'.format(o.std))
    o.price()

    if args.plot=='True':
        o.build_path()
        plt.title('Average simulaated stock price')
        plt.ylabel('price')
        plt.plot(o.results[:,-100:].T);
