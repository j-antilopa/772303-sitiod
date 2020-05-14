import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import sklearn as sklearn
import statsmodels.api as sm

x = np.array([5, 20, 30, 40, 55, 60, 68, 72]).reshape((-1, 1))  # двумерный массив
y = np.array([5, 22, 16, 24, 55, 46, 63, 77])

model = LinearRegression().fit(x, y)

rsquare = model.score(x, y)
print('Rsquare: ', rsquare)

coef = model.coef_
print('Coefficient:', coef)

y_predict = model.predict(x)
print('Predict for x: ', y_predict)

mean = sklearn.metrics.mean_squared_error(y, y_predict)
print('Mean squared error: ', mean)

plt.scatter(x, y,  color='blue')
plt.plot(x, y_predict, color='red', linewidth=4)
plt.show()

ols_model = sm.OLS(x, y)
ols_results = ols_model.fit()
print(ols_results.summary())