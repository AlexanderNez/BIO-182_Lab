import statsmodels.api as sm

data = {
        'cushion' : [40, 39, 39, 41, 44, 44, 46, 39, 37, 39, 38, 42, 38, 36, 38, 37, 43, 42, 36, 39, 39, 40, 41, 43],
        'table' : [55, 55, 57, 60, 57, 59, 60, 61, 59, 59, 59, 62, 60, 60,
                       58, 57, 59, 60, 60, 59, 59, 60, 60, 60]
        }

x = data['table']
y = data['cushion']
    
model = sm.OLS(y,x)
fit = model.fit()
Sum = fit.summary()
    
print(Sum)