"""
matrixmath.py
 Operaciones matriciales en Python
"""
import numpy as np

a = np.array( [[ -5.1, 3.8, 4.2 ], \
              [ 9.7, 1.3, -1.3]] )

b = np.empty( [3,2])
b[:, 0] = [9.4, -6.2, 0.5 ]
b[:, 1] = [-5.1, 3.3, -2.2]

print("Matrix a")
print(a)
print("Matrix b")
print(b)

c = np.matmul(a, b) 
print ("matmul(a,b)")
print (c)

c = np.matmul(b,a)
print ("matmul(b,a)")
print (c)

print("Valor max de a ", np.amax(a))
loc2 = np.argmax(a)
loc1 = np.unravel_index(loc2, np.shape(a))
print("Posición del max of a", loc1)
print("Max(a) con su posición", a[loc1])

c = a + np.transpose(b)
print("Matrix a + transpose(b)")
print(c)

print("a shape ", np.shape(a))
print("b shape ", np.shape(b))

print("a size  ", np.size(a))
print("b size  ", np.size(b))


