#mandel1.py
#Grafica el set mandelbrot para un número de puntos

import cmath as cm
import numpy as np
import matplotlib.pyplot as plt

x1,x2,y1,y2 = input('Ingrese x1,x2,y1,y2:  ').split()
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

#define el tamaño de malla y comienzo de matriz

nx = 100
ny = 100
dx = (x2-x1)/float(nx)
dy = (y2-y1)/float(ny)
dat = np.zeros((nx,ny))

#Loop principal para cada valor
for ix in range(nx):
    for iy in range(ny):
        cr = x1 + dx/2. + dx*float(ix)
        ci = y1 + dy/2. + dy*float(iy)
        #crea el número complejo
        c = complex(cr,ci)
        z = complex(0.0, 0.0)
        for it in range(10000):
            z = c + z*z
            if (abs(z) > 2):
                break
            dat[ix,iy] = it+1

#Rota la matriz y grafica en escala log10
dat = np.transpose(dat)
zdat = np.log10(dat)

#graficar resultado
plt.imshow(zdat,interpolation='bilinear',extent=(x1,x2,y1,y2),cmap='nipy_spectral')
plt.axis('equal')
plt.savefig('mandel1.png')
plt.show()

