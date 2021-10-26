"""
testcomplex.py
""" 
import numpy as np

zreal = np.random.randint(1,5)
zimag = np.random.randint(1,5)
a = complex(float(zreal),float(zimag))
b = complex(2,1)

c    = a*b
csq  = np.sqrt(c)
csin = np.sin(c)
cexp = np.exp(c)

print('# complejo a    =', a)
print('# complejo b    =', b)
print('c = a x b       =', c)
print('|c|             = %.2f' % abs(c))
print('sqrt(c)         = (%.2f, %.2fj)' %(csq.real,csq.imag))
print('sin(c)          = (%.2f, %.2fj)' %(csin.real,csin.imag))
print('exp(c)          = (%.2f, %.2fj)' %(cexp.real,cexp.imag))


