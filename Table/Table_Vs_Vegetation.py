import statsmodels.api as sm

data = {
        'table' : [55, 55, 57, 60, 57, 59, 60, 61, 59, 59, 59, 62, 60, 60,
                       58, 57, 59, 60, 60, 59, 59, 60, 60, 60],
        'Vegetation' : [22, 17, 33, 28, 25, 29, 40, 10, 13, 24, 13, 19, 21, 20,
                        8, 12, 13, 12, 44, 29, 18, 23, 40, 34]
        }

x = data['table']
y = data['Vegetation']
    
model = sm.OLS(y,x)
fit = model.fit()
Sum = fit.summary()
    
print(Sum)