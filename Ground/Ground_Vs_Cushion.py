import statsmodels.api as sm

data = {
        'cushion' : [40, 39, 39, 41, 44, 44, 46, 39, 37, 39, 38, 42, 38, 36, 38, 37, 43, 42, 36, 39, 39, 40, 41, 43],
        'ground' :[55, 20, 30, 33, 55, 30, 47, 54, 50, 25, 8, 16, 56, 49,
                        54, 56, 53, 46, 9, 51, 54, 50, 27, 33],
        }

x = data['ground']
y = data['cushion']
    
model = sm.OLS(y,x)
fit = model.fit()
Sum = fit.summary()
    
print(Sum)