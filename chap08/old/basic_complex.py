# basic_complex.py
# Some basic complex number concepts

import cmath

z0 = 1j
z1 = 1j * 1j

print(z0)
print(z1)

z0 =  complex(2,3)
z  = 2+3j
print(z, z0)

print(z.real)
print(z.imag)
print(z.conjugate())

z = complex(3,4)
print(z, abs(z))
print(pow(z, 2))

# Some function on complex
print("Functions on complex numbers")
z = complex(2,3)
zsin = cmath.sin(z)
zcos = cmath.cos(z)

print('For z = ', z)
print('cos(z), sin(z)', zcos, zsin)
