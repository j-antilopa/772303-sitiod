


# Создаём векторы x, y
x <- c(9, 5, 8, 2, 1)
y <- c(53, 20, 4, 31, 19)

# Рисуем диаграмму
plot(x,y,main="Correlation x | y")

# Высчитываем саму корелляцию
correlation <- cor(x, y)
correlation

# Найдём наклон 'k' и 'b'  ( y = kx + b )
dataframe <- lm(y ~ x)
//dataframe

# Нарисуем линию регрессии
abline(dataframe)

# k в (y = kx + b)
k <- dataframe$coefficients[[1]]
k

# b в (y = kx + b)
b <- dataframe$coefficients[[2]]
b

# Находим Остатки
res <- residuals(dataframe)
res
# Строим из них график
 plot(x,res)


summary(dataframe)
