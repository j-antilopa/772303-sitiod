import numpy as np
import random

if __name__ == "__main__":
    vector = np.array([random.randint(0, 20) for i in range(20)])
    print(f'{vector=}')
    print(f'{vector*2=}')
    print(f'{vector+2=}')
    print(f'Сумма всех элементов: {np.sum(vector)=}\n'
          f'Минимальное: {np.min(vector)=}\n'
          f'Максимальное: {np.max(vector)=}\n'
          f'Перемножение всех элементов вектора: {np.prod(vector)=}\n' 
          f'Размер вектора: {np.size(vector)=}\n'
          f'Среднее арифметическое: {np.mean(vector)=}\n'
          f'Вариация: {np.var(vector)=}\n' 
          f'Отсортированный вектор: {np.sort(vector)=}\n')
