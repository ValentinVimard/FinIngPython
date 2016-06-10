# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:54:44 2016

@author: Valentin
"""

from datetime import date
import os
import pandas as pd
import numpy as np
from derivative import derivative,print_aux


path=os.path.dirname(os.path.realpath(__file__))
file = os.path.join(path,"Portfolio_Project2.xls") 



#___________________________________________________________________________#
# --------------------------------------------------------------------------#     
#   Fonction use to print vectors  
#        INPUT :
#                an numpy array
#        OUTPUT :
#                none
#       ASSIGN :
#               print the elements of the array
# --------------------------------------------------------------------------#  
#___________________________________________________________________________#


class portfolio :
#___________________________________________________________________________#
# --------------------------------------------------------------------------#     
#    Initialise the portfolio, downloading the values from the excel sheet  
#        INPUT :
#                none
#        OUTPUT :
#                object Portfolio composed by the six derivatives
# --------------------------------------------------------------------------#     
    def __init__(self):
        self.ps = derivative(date(2015,9,16),0.007,0,np.asarray(pd.read_excel(file,header=None, skiprows=10,parse_cols="B")))
        self.rs = derivative(date(2015,9,2),0.012,0,np.asarray(pd.read_excel(file,header=None, skiprows=10,parse_cols="C")))
        self.sc = derivative(date(2015,8,7),0.0035,0,np.asarray(pd.read_excel(file,header=None, skiprows=10,parse_cols="D")))
        self.lc = derivative(date(2015,7,20),0.0062,0,np.asarray(pd.read_excel(file,header=None, skiprows=10,parse_cols="E")))
        self.lf = derivative(date(2015,7,7),-0.003,0,np.asarray(pd.read_excel(file,header=None, skiprows=10,parse_cols="F")))
        self.ldf = derivative(date(2015,7,7),-0.0045,0.02,np.asarray(pd.read_excel(file,header=None, skiprows=10,parse_cols="G")))
#___________________________________________________________________________#
        
#___________________________________________________________________________# 
# --------------------------------------------------------------------------# 
#    Give the matrix of all the notionals
#        INPUT :
#                a portfolio
#        OUTPUT :
#                a numpy matrix 40 x 7
# --------------------------------------------------------------------------# 
       
    def notionals(self):
        ps = self.ps.notionals.copy()
        rs = self.rs.notionals.copy()
        sc = self.sc.notionals.copy()
        lc = self.lc.notionals.copy()
        lf = self.lf.notionals.copy()
        ldf= self.ldf.notionals.copy()
        
#        resizing to have rows of 40 elements
        
        ps.resize(40)
        rs.resize(40)
        sc.resize(40)
        lc.resize(40)
        lf.resize(40)
        ldf.resize(40)
        
        return np.array([ps,rs,sc,lc,lf,lf,ldf]).reshape((7,40)).transpose()
#___________________________________________________________________________#
        


#___________________________________________________________________________# 
# --------------------------------------------------------------------------# 
#    Give the vector of  the trade dates
#        INPUT :
#                a portfolio
#        OUTPUT :
#                a vector 1x7
# --------------------------------------------------------------------------#         
    def trade_dates(self) :
         return np.array([self.ps.T0,self.rs.T0,self.sc.T0,self.lc.T0,self.lf.T0,self.lf.T0,self.ldf.T0])
#___________________________________________________________________________# 
 
#___________________________________________________________________________#        
# --------------------------------------------------------------------------# 
#    Give the vector of  the strikes
#        INPUT :
#                a portfolio
#        OUTPUT :
#                a vector 1x7
# --------------------------------------------------------------------------# 
    def strikes (self):
        return np.array([self.ps.strike,self.rs.strike,self.sc.strike,self.lc.strike,self.lf.strike,self.lf.strike,self.ldf.strike])
#___________________________________________________________________________# 
        
#___________________________________________________________________________# 
# --------------------------------------------------------------------------# 
#    Give the vector of  the digital payoff
#        INPUT :
#                a portfolio
#        OUTPUT :
#                a vector 1x7
# --------------------------------------------------------------------------# 
    def digital_payoffs(self) :
        return np.array([self.ps.digital_payoff,self.rs.digital_payoff,self.sc.digital_payoff,self.lc.digital_payoff,self.lf.digital_payoff,self.lf.digital_payoff,self.ldf.digital_payoff])
#___________________________________________________________________________#        

#___________________________________________________________________________#         
# --------------------------------------------------------------------------# 
#    Give the vector of  the trade dates
#        INPUT :
#                a portfolio
#        OUTPUT :
#                none
#       ASSIGN : 
#                print all the elements of the portfolio
# --------------------------------------------------------------------------# 
    def print(self) :   
        print("Trading Dates : ")
        print_aux(self.trade_dates())
        print("Strikes : ")
        print_aux(self.strikes())
        print("Digital payoffs : ")
        print_aux(self.digital_payoffs())
        print ("Notionals : ")
        print(self.notionals())
#___________________________________________________________________________# 
    
#end class
#___________________________________________________________________________#
