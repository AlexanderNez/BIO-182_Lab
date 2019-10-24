import pandas as pd
import numpy as py
import os
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf


mydir = os.path.expanduser('~/Desktop/Dine College/SY-2019/Fall-2019')

data = {
        'cushion' : [40, 39, 39, 41, 44, 44, 46, 39, 37, 39, 38, 42, 38, 36, 38, 37, 43, 42, 36, 39, 39, 40, 41, 43],
        'Vegetation' : [22, 17, 33, 28, 25, 29, 40, 10, 13, 24, 13, 19, 21, 20,
                        8, 12, 13, 12, 44, 29, 18, 23, 40, 34]
        }

x = data['cushion']
y = data['Vegetation']
   
model = sm.OLS(y,x)
fit = model.fit()
Sum = fit.summary()
    
Treatment = pd.DataFrame(data)
    
T_Statistic = Treatment.describe()
    
    
Correlation = Treatment.corr(method = 'pearson')

print(model)
print(fit)
print(Sum)
print(T_Statistic)
print(Correlation)