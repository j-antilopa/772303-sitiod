# Create vector x, y
x <- c(1, 3, 5, 7, 9)
y <- c(13, 27, 34, 47, 51)

# Draw diagram x, y
plot(x,y,main="Correlation x | y")

# Calculate correlation
correlation <- cor(x, y)

# Find 'k' slope and 'b' intercept in ( y = kx + b )
dataframe <- lm(y ~ x)

# Draw line of linnear regression by fit
abline(dataframe)

# k in (y = kx + b)
k <- dataframe$coefficients[[1]]

# b in (y = kx + b)
b <- dataframe$coefficients[[2]]

# Residuals of linnear regression
residuals(dataframe)

# Also residuals
dataframe$residuals

# Draw points of residuals
 plot(x,fit$residuals)

# Print summary of dataframe
summary(dataframe)