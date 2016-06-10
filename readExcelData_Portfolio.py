# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:54:44 2016

@author: Valentin
"""

from datetime import date
import os
import pandas as pd
import numpy as np
import derivative as der
import datetime 

path=os.path.dirname(os.path.realpath(__file__))
file = os.path.join(path,"Portfolio_Project2.xls") 

class portfolio :
    
    def __init__(self):
        self.ps = der.derivative(date(2015,9,16),0.007,0,np.asarray(pd.read_excel(file,header=None, skiprows=10,parse_cols="B")))
        self.rs = der.derivative(date(2015,9,2),0.012,0,np.asarray(pd.read_excel(file,header=None, skiprows=10,parse_cols="C")))
        self.sc = der.derivative(date(2015,8,7),0.0035,0,np.asarray(pd.read_excel(file,header=None, skiprows=10,parse_cols="D")))
        self.lc = der.derivative(date(2015,7,20),0.0062,0,np.asarray(pd.read_excel(file,header=None, skiprows=10,parse_cols="E")))
        self.lf = der.derivative(date(2015,7,7),-0.003,0,np.asarray(pd.read_excel(file,header=None, skiprows=10,parse_cols="F")))
        self.ldf = der.derivative(date(2015,7,7),-0.0045,0.02,np.asarray(pd.read_excel(file,header=None, skiprows=10,parse_cols="G")))
    
    
    def yf(self,t):
        return ((datetime.toordinal(t)-datetime.toordinal(self.T0))/365)


     

