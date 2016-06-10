# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:21:41 2016

@author: Valentin
"""
from datetime import datetime
import pandas as pd
import numpy as np
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
import scipy.stats as ss
from datetime import date

def year_to_date(settlement,year):
      return (datetime.toordinal(settlement)+ year*(365))
      
def year_frac (settlement, t):
      return ((datetime.toordinal(t) - datetime.toordinal(settlement))/365)

#___________________________________________________________________________#
class derivative :

#___________________________________________________________________________#
# --------------------------------------------------------------------------#     
#   Initiate a derivative 
#        which can be swaps , floors, cap...
  
#        INPUT :
#               T0 :                the trading date of the derivative
#               strike:            its strike
#               digital_payoff :   its digital payoff ( if it's a digital derivative)
#               notionals :        a numpy array with all the notionals (amortized in 10 years maximum)
#        OUTPUT :
#                the object derivative with all these values.

# --------------------------------------------------------------------------# 

    def __init__(self,T0,strike,digital_payoff,notionals) :
        self.T0 = T0
        self.strike = strike
        self.notionals = notionals
        self.digital_payoff = digital_payoff
#___________________________________________________________________________#
        
#___________________________________________________________________________#
# --------------------------------------------------------------------------#     
#   print  a derivative 
  
#        INPUT :
#                  a derivative
#        OUTPUT :
#                none
#          ASSIGN : 
#                  the derivative printed

# --------------------------------------------------------------------------#         
    def print(self):
        print(self.T0)
        print(self.strike)
        print(self.digital_payoff)
        print(self.notionals)
#___________________________________________________________________________#
        
        
#end class derivative     
#___________________________________________________________________________#
        