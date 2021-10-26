"""
testmatriz.py
programa con algunos ejemplos de matrices 2D
"""
import numpy as np

y = np.empty([2, 3])
print('Empty Y float ')
print(y)

x = np.zeros([2,3],dtype=int)
print('Zeros X enteros')
print(x)

x[0,:] = [1, 2, 3]
x[1,:] = [4, 5, 6]
print('X unidades')
print (x)

x = x + 1
print('X mas 1')
print(x)

c = np.array( [ [1,2], [3,4] ], dtype=complex )
print('Matriz compleja')
print(c)


