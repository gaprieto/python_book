# testcomplex2.py

import cmath

zreal = input("Enter real part ")
zimag = input("Enter imaginary part ")

a = complex(float(zreal),float(zimag))
print ('z = ', a)

a = cmath.exp(a)
print ('exp(a) = ', a)

print ('Real and Imaginary parts ', a.real, a.imag)
