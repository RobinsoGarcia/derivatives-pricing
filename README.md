

python options_pricing.py -s IBM -K 155 -T 2019-4-2 -t european

parser.add_argument("-i","--iterations",type=int,default=5,help="Set the number of iterations, improves the result. The goal is to see little price changes one simulation after the other.")
