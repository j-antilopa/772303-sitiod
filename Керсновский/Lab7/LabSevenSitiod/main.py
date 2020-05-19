import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import statsmodels.api as sm

x = np.array([2, 12, 33, 41, 42, 55, 58, 70, 77, 75]).reshape((-1, 1))
y = np.array([1, 8, 11, 15, 20, 33, 34, 40, 44, 40])

model = LinearRegression().fit(x, y)

print(f'Коэфициент детерминации{model.score(x, y)}')

predict = model.predict(x)
print('Предстказанное значение: ', predict)

plt.scatter(x, y,  color='b')
plt.plot(x, predict, color='r')
plt.show()

ols_model = sm.OLS(x, y)
ols_res = ols_model.fit()
print(ols_res.summary())