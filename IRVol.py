# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 19:00:12 2016

@author: Valentin
"""
from datetime import datetime
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt 
import scipy.stats as ss
from datetime import date
from derivative import year_to_date,year_frac



path=os.path.dirname(os.path.realpath(__file__))
file = os.path.join(path,"IRVol.xls")       
#      
#%% Dates

class dates:
    def __init__(self) :     
        self.settlement = date(2016,4,12)
        self.depos = year_to_date(self.settlement,0.25)
        self.swaps = np.append(np.arange(11),np.array((12,15,20,25,30)))
    
    def print(self):
        print(self.settlement)

        
#%% Rates 
#depos = xlsread( filename, 'Data', 'J85' ); % depos rates 
#swaps = xlsread( filename, 'Data', 'O80:O94' );  % swaps rates
#
#rates = struct ( 'depos', depos, 'swaps', swaps );

class rates :
    def __init__(self):
        self.depos = -0,248
        self.swaps = np.asarray(pd.read_excel(file,header=None, skiprows=80,parse_cols="O"))
        




