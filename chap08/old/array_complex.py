# array_complex.py

import cmath
import numpy as np

a = np.array([1+2j, 3+4j, 5+6j])

print('Complex array ', a.shape)
print(a)

print ('Imag part ', a.imag)
a.imag = np.array([8, 10, 12])

print('New array ', a)

a = np.array([1+2j, 3+4j, 5+6j])
a = a[:, np.newaxis]
b = a.T

print('Array a, (3,1) ', a)
print('Array b, (1,3) ', b)

c = np.matmul(a,b)

print ('matmul(a*a.T)')
print(c)

c = np.matmul(a,np.conjugate(b))

print ('matmul(a*conj(a.T))')
print(c)



