import statsmodels.api as sm

data = {
        'table' : [55, 55, 57, 60, 57, 59, 60, 61, 59, 59, 59, 62, 60, 60,
                       58, 57, 59, 60, 60, 59, 59, 60, 60, 60],
        'ground' :[55, 20, 30, 33, 55, 30, 47, 54, 50, 25, 8, 16, 56, 49,
                        54, 56, 53, 46, 9, 51, 54, 50, 27, 33],
        }

x = data['table']
y = data['ground']
    
model = sm.OLS(y,x)
fit = model.fit()
Sum = fit.summary()
    
print(Sum)