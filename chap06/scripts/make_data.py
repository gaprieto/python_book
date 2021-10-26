"""
Programa para crear los datos del Capítulo 06
"""

import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

v = np.linspace(0, 20, 100)

b0 = sp.jn(0,v)
b2 = sp.jn(0,1.5*v)

M = np.transpose(np.vstack((v,b0,b2)))

print(np.shape(M))

np.savetxt('data/some_data.dat', M,fmt='%6.2f %6.3f %6.3f')

fig = plt.figure(1)
plt.plot(v,b0)
plt.plot(v,b2)

npts = 720
v = np.linspace(0, 720, npts)
xrd = np.random.randn(npts)*0.01
yrd = np.random.randn(npts)*0.01

b0 = np.cos(v/180.*np.pi)+xrd
b2 = np.sin(v/180.*np.pi)+yrd

M = np.transpose(np.vstack((v,b0,b2)))
np.savetxt('data/some_data_header.dat', M,
            header='  theta       cos       sin',
            fmt='%9.2e %9.2e %9.2e')


fig2 = plt.figure(2)
plt.plot(v,b0)
plt.plot(v,b2)

npts = 40
b0 = np.random.randn(npts)+5.0
b2 = np.random.randn(npts)-3.0

M = np.transpose(np.vstack((b0,b2)))
np.savetxt('data/another_data.dat', M,
            fmt='%8.4f %8.4f')


fig3 = plt.figure(3)
plt.plot(b0)
plt.plot(b2)


plt.show()


