# testarray.py
# Program showing simple array handling

import numpy as np

x = np.array([1, 2, 3])
y = np.ones(3)
z = np.ones(3)*2
print (x)
print (y)
print (z)

x[1] = 15
y[:] = 2
z    = z-1

print(x)
print(y)
print(z)

