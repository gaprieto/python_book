# testmatrix.py
# Program showing simple matrix array handling

import numpy as np


x = np.empty((2, 3),dtype=int)
print (x)

x[0,:] = [1, 2, 3]
x[1,:] = [4, 5, 6]

print (x)

x = x + 1
print(x)

c = np.array( [ [1,2], [3,4] ], dtype=complex )
print(c)

