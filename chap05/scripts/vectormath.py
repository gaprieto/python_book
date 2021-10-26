"""
vectormath.py
 Programa mostrando operaciones aritméticas
 con arreglos en Python
"""
import numpy as np

a = np.array( [1., 2., 3., 4., 5.] )
b = np.ones(5)*2

print("a     = ", a)

c = a + 1
print("a + 1 = ", c)

c = 2 * a
print("2 * a = ", c)

c = a * a
print("a * a = ", c)

print('')
c = np.sqrt(a)
print("sqrt(a) = ", c)

c = np.sin(a)
print("sin(a) = ", c)

c = np.exp(a)
print("exp(a) = ", c)

print('')
print("a = ", a)
print("b = ", b)

c = a + b
print("a + b = ", c)

c = a * b
print("a * b = ", c)

print('')
x = np.sum(a)
print("sum(a) = ", x)

c = a
c[3:5] = 0.0
print ("a con dos ceros al final", c )

x = np.dot(a,b)
print ("a dot b = ", x)

print('')
x = np.sum((a - np.sum(a)/5.)**2)
print ("suma del cuadrado de las diferencias del promedio = ", x)


