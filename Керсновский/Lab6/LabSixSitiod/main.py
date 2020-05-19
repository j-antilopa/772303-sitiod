import numpy as np
import matplotlib.pyplot as plot

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
# Задаём сетку на графике
plot.grid(True, which='both')
# Устанавливаем линию с координатой y=0, красным цветом
plot.axhline(y=0, color='r')

# Задаём график
plot.plot(x, np.tan(x))

# Высота оси y
plot.ylim(-10, 10)

# Задаём заголовок
plot.title('tangent')
# Подпись ос x
plot.xlabel('x')
# Подпись оси y
plot.ylabel('tg(x)')

plot.show()

# Создаём и выводим диагональную матрицу
print(f'Диагональная матрица: \n{np.diag(np.arange(1, 6))}')

# Строим четырёхмерный массив и выводим его по срезам
arr = np.random.randint(0, 10, (2, 3, 2, 3))
print(f'Исходный массив: \n{arr}')

# Сложение с числом
arr2 = np.random.randint(0, 10, (2, 3, 2, 3))
print(f'Сложение с  числом: \n{arr + 2}\n'
      f'Сложение с массивом: \n{arr + arr2}\n'
      f'Возведение в степень: \n{np.power(arr, 2)}\n'
      f'Умножение на другой массив: \n{arr * arr2}\n'
      f'Трансонирование: \n{np.transpose(arr)}\n')

# Решение системы A*X=b
A = np.random.randint(0, 10, (4, 4))
B = np.random.randint(0, 10, 4)
X = np.linalg.solve(A, B)
print(f'{A=}\n\n'
      f'{B=}\n\n'
      f'{X=}')
