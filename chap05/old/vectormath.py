# vectormath.py
# Program showing arithmetic operations with arrays
# in Python

import numpy as np
#import math as mt

a = np.array( [1., 2., 3., 4., 5.] )
b = np.ones(5)*2

print("a = ", a)

c = a + 1
print("a + 1 = ", c)

c = 2 * a
print("2 * a = ", c)

c = a * a
print("a * a = ", c)

c = np.sqrt(a)
print("sqrt(a) = ", c)

c = np.sin(a)
print("sin(a) = ", c)

c = np.exp(a)
print("exp(a) = ", c)

print("b = ", b)

c = a + b
print("a + b = ", c)

c = a * b
print("a * b = ", c)

x = np.sum(a)
print("sum(a) = ", x)

c = a
c[3:4] = 0.0
print ("a with two zeros at end", c )

x = np.dot(a,b)
print ("a dot b = ", x)

x = np.sum((a - np.sum(a)/5.)**2)
print ("sum of squares of difference from mean = ", x)

