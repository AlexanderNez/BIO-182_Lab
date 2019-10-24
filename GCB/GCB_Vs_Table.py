import statsmodels.api as sm

data = {
        'floor' : [51, 55, 60, 50, 50, 53, 55, 54, 53, 58, 57, 56, 56, 58, 
                       58,56, 55, 58, 57, 59, 60, 58, 58, 58],
        'table' : [55, 55, 57, 60, 57, 59, 60, 61, 59, 59, 59, 62, 60, 60,
                       58, 57, 59, 60, 60, 59, 59, 60, 60, 60],
        }

x = data['floor']
y = data['table']
    
model = sm.OLS(y,x)
fit = model.fit()
Sum = fit.summary()

print(Sum)