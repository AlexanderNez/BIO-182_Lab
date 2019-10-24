import statsmodels.api as sm

# import Analysis_Ball_and_Stick as BIO

data = {
            'floor' : [51, 55, 60, 50, 50, 53, 55, 54, 53, 58, 57, 56, 56, 58, 
                           58,56, 55, 58, 57, 59, 60, 58, 58, 58],
            'ground' :[55, 20, 30, 33, 55, 30, 47, 54, 50, 25, 8, 16, 56, 49,
                            54, 56, 53, 46, 9, 51, 54, 50, 27, 33],
            }

x = data['floor']
y = data['ground']
    
model = sm.OLS(y,x)
fit = model.fit()
Sum = fit.summary()
    
print(Sum)