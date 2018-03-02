from derivatives_pricing.securities import derivatives as dv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import *
import sys
import json
from datetime import date,time

c = dv.call('AAPL',170,'2018-03-29')

iguess = c.std
f = dv.BS(S=c.S0,K=c.K,r=c.rf,
std=c.std,t=c.T,option_type=c.option_type1)

zGuess = iguess

a = fsolve(f,zGuess)
