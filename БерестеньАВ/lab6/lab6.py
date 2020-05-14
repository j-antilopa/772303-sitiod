import numpy as np
import matplotlib.pyplot as plot

# First task
# Create a graph of any trigonometric function(Cosine) with a plot() function

# Create array for trigonometric function with 0.1 step
timeline = np.arange(0, 20, 0.1)

# Calculate cosine
amplitude = np.cos(timeline)

# Graph visualization setup
plot.plot(timeline, amplitude)

# Legend
plot.title('Cosine wave')

# X
plot.xlabel('x')

# Amplitude
plot.ylabel('Amplitude = cos(x)')
plot.grid(True, which='both')
plot.axhline(y=0, color='r')
plot.show()

# Second task
# Creating matrix with diag()
diagMatrix = np.arange(6)
print(str(np.diag(diagMatrix)))

# Third task
# Four-dimensional array
array = np.arange(81).reshape(3, 3, 3, 3)
print('Start array: \n' + str(array))

# Fourth task(operations)
print('After plus with number: \n' + str(array + 10))
arrayForOperations = np.arange(100, 181, 1).reshape(3, 3, 3, 3)
print('Plus with array: \n' + str(array + arrayForOperations))
print('Exponentiation : \n' + str(np.power(array, 2)))
print('Multiplying with array : \n' + str(array * arrayForOperations))
print('Transpose: \n' + str(np.transpose(array)))

# Fifth task(A*X=b)
A = np.array([[3, -9], [2, 4]])
b = np.array([-42, 2])
x = np.linalg.solve(A, b)
print('\n\n\nA : \n' + str(A))
print('B : ' + str(b))
print('x:' + str(x))
