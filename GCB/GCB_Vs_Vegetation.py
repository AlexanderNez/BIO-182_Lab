import statsmodels.api as sm

data = {
        'floor' : [51, 55, 60, 50, 50, 53, 55, 54, 53, 58, 57, 56, 56, 58, 
                       58,56, 55, 58, 57, 59, 60, 58, 58, 58],
        'Vegetation' : [22, 17, 33, 28, 25, 29, 40, 10, 13, 24, 13, 19, 21, 20,
                        8, 12, 13, 12, 44, 29, 18, 23, 40, 34]
        }

x = data['floor']
y = data['Vegetation']
    
model = sm.OLS(y,x)
fit = model.fit()
Sum = fit.summary()

print(Sum)