"""
array_complex.py
""" 
import numpy as np

a = np.array([1+2j, 3+4j, 5+6j])
a = a[:, np.newaxis]
b = a.T

print('Arreglo a, shape ',np.shape(a))
print( a)
print('Arreglo b, shape ',np.shape(b))
print( b)
c = np.matmul(a,b)

print ('matmul(a*a.T)')
print(c)

c = np.matmul(a,np.conjugate(b))

print ('matmul(a*conj(a.T))')
print(c)

c = np.matmul(a,np.conjugate(b))

print ('sqrt(c)')
np.set_printoptions(precision=3)
print(np.sqrt(c))

