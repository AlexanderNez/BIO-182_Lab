import statsmodels.api as sm

data = {
        'ground' :[55, 20, 30, 33, 55, 30, 47, 54, 50, 25, 8, 16, 56, 49,
                        54, 56, 53, 46, 9, 51, 54, 50, 27, 33],
        'Vegetation' : [22, 17, 33, 28, 25, 29, 40, 10, 13, 24, 13, 19, 21, 20,
                        8, 12, 13, 12, 44, 29, 18, 23, 40, 34]
        }

x = data['ground']
y = data['Vegetation']
    
model = sm.OLS(y,x)
fit = model.fit()
Sum = fit.summary()
    
print(Sum)