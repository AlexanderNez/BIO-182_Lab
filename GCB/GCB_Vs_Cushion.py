import statsmodels.api as sm


data = {
        'floor' : [51, 55, 60, 50, 50, 53, 55, 54, 53, 58, 57, 56, 56, 58, 
                       58,56, 55, 58, 57, 59, 60, 58, 58, 58],
        'cushion' : [40, 39, 39, 41, 44, 44, 46, 39, 37, 39, 38, 42, 38, 36, 38,
                     37, 43, 42, 36, 39, 39, 40, 41, 43]        
        }

x = data['floor']
y = data['cushion']
    
model = sm.OLS(y,x)
fit = model.fit()
Sum = fit.summary()

print(Sum)