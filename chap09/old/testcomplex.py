# testcomplex.py

import cmath

zreal,zimag = input("Enter first  complex number ").split()
a = complex(float(zreal),float(zimag))

zreal,zimag = input("Enter second complex number ").split()
b = complex(float(zreal),float(zimag))

c = a*b

print('Product         = ', c)
print('abs of product  = ', abs(c))
print('sqrt of product = ', cmath.sqrt(c))

