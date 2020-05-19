# Создаем последовательность чисел
x_coordinates <- seq(0, 60, by = 0.2)

# Рисуем диаграмму косинусов
plot(x_coordinates, cos(x_coordinates), xlab = "x", ylab = "y", main = "sin(x)")

# Создаём диагональную матрицу
diag(5)

# Создаём четырёхмерную матрицу
z <- array(1:3, dim = c(3, 3, 3, 3))

# Прибавляем к ней 6
add <- z + 6
add

# Добавляем вектор (1, 2, 3) к матрице
add_sec <- z + seq(1:3)
add_sec

# Возводим в стпень 3
pow <- z ^ 3
pow

# Умножаем на вектор (1, 2, 3)
mult_sec <- z * seq(1:3)
mult_sec

# Транспонируем
transpose <- aperm(z)
transpose

# Создаем 3x3 матрицу
A1 <- matrix(c(4, 6, 3,
               8, 1, 8,
               5,  4, 9), 3, 3, byrow=TRUE)

# Создаем 3x1 матрицу
b1 <- matrix(c(55, 1, -8), 3, 1)

# Умножаем матрицы A*X=b
solution <- solve(A1, b1)

# Проверка
b2 <- A1 %*% solution

b2
