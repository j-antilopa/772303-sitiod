"lab 6"
x_coordinates <- seq(0, 40, by = 0.1)
plot(x_coordinates, sin(x_coordinates), xlab = "xs", ylab = "ys", main = "sinus function")
diag(3)
strrep("nvm", 30)
ar <- array(1:5, dim = c(3, 3, 3, 3))
ar
strrep("nvm", 3)
"Add 2"
ar + 2
strrep("nvm", 3)
"Add array"
ar + array(2:6, dim = c(3, 3, 3, 3))
strrep("nvm", 3)
"2 power"
ar^2
strrep("nvm", 3)
"Mult array"
ar * c(3, 6, 7)
strrep("nvm", 3)
"Transpose "
aperm(ar)
strrep("nvm", 3)
a <- matrix(c(2, 1, -1,
              -3, -1, 2,
              -2, 1, 2), 3, 3, byrow = TRUE)
b <- c(8, -11, -3)
x <- solve(a, b)
x
a %*% x


