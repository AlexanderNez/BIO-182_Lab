import pandas as pd
import numpy as py
import os
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

# import GCB_Vs_Ground as GVF

mydir = os.path.expanduser('~/Desktop/Dine College/SY-2019/Fall-2019')

cold_data = {'cold bounce' : [32, 28, 30, 32, 34, 37, 35, 31, 37, 39, 36, 37, 34, 36,
                         36, 32, 39, 40, 40, 41, 42, 42, 41, 40, 41, 41, 40, 42,
                         41, 44, 43, 43, 44, 44, 41, 44, 42, 44, 45, 46, 47, 45,
                         43, 45, 46, 46, 48, 46, 47, 46] }

data = {
        'floor' : [51, 55, 60, 50, 50, 53, 55, 54, 53, 58, 57, 56, 56, 58, 
                       58,56, 55, 58, 57, 59, 60, 58, 58, 58],
        'cushion' : [40, 39, 39, 41, 44, 44, 46, 39, 37, 39, 38, 42, 38, 36, 38, 37, 43, 42, 36, 39, 39, 40, 41, 43],
        'table' : [55, 55, 57, 60, 57, 59, 60, 61, 59, 59, 59, 62, 60, 60,
                       58, 57, 59, 60, 60, 59, 59, 60, 60, 60],
        'ground' :[55, 20, 30, 33, 55, 30, 47, 54, 50, 25, 8, 16, 56, 49,
                        54, 56, 53, 46, 9, 51, 54, 50, 27, 33],
        'Vegetation' : [22, 17, 33, 28, 25, 29, 40, 10, 13, 24, 13, 19, 21, 20,
                        8, 12, 13, 12, 44, 29, 18, 23, 40, 34]
        }
        
Treatment = pd.DataFrame(data)
Cold = pd.DataFrame(cold_data)

T_Statistic = Treatment.describe()
C_Statistic = Cold.describe()

Correlation = Treatment.corr(method = 'pearson')

x = data['floor']
y = data['ground']
    
model = sm.OLS(y,x)
fit = model.fit()
Sum = fit.summary()
    
d_floor = data['floor']
    
print(Sum)
'''
print(Correlation)

print(Cold)
print(Treatment)

print(T_Statistic)
print(C_Statistic)
'''