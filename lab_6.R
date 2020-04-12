# Create seq of x coordinates
x_coordinates <- seq(0, 40, by = 0.1)

# Draw cos diagram
plot(x_coordinates, cos(x_coordinates), xlab = "x", ylab = "y", main = "sin(x)")

# Create diagonal matrix
diag(6)

# Create 4th dimensional matrix
z <- array(1:3, dim = c(3, 3, 3, 3))

# Add 5 to matrix
add <- z + 5

# Add vector (1, 2, 3) to matrix
add_sec <- z + seq(1:3)

# Power by 2
pow <- z ^ 2

# Mult matrix by vector (1, 2, 3)
mult_sec <- z * seq(1:3)

# Transpose 4th dimensional matrix
transpose <- aperm(z)

# Create matrix 3x3
A1 <- matrix(c(6, 3, -3,
               -9, -3, 6,
               -6,  3, 6), 3, 3, byrow=TRUE)

# Create matrix 3x1
b1 <- matrix(c(24, -33, -9), 3, 1)

# Solve A*X=b
solution <- solve(A1, b1)

# Prove solution
b2 <- A1 %*% solution

b2

