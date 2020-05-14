import random

import numpy as np
vector = np.array([random.randint(0, 10) for i in range(10)])
print("Default vector " , vector)
vector *= 2
print("After multiplication by 2 ",vector)
vector += 2
print("After addition 2 ",  vector)
print("Sum " , np.sum(vector))
print("Min " ,  np.min(vector))
print("Max " ,  np.max(vector))
print("Prod ",  np.prod(vector))
print("Size ",  np.size(vector))
print("Mean",  np.mean(vector))
print("Var ",  np.var(vector))
print("Sort ", np.sort(vector))
