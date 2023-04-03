# Code to make synthetic data for 
# 3D plotting

import numpy as np

# define normalized 2D gaussian
def gaus2d(x=0, y=0, mx=0, my=0, sx=1, sy=1):
    
    gfun1 = 1. / (2. * np.pi * sx * sy) 
    gfun2 = np.exp(-((x - mx)**2. / (2. * sx**2.) + (y - my)**2. / (2. * sy**2.)))
    gfun  = gfun1 * gfun2

    return gfun

# Create data

N = 45
x = np.linspace(-3,3,N)
y = np.linspace(-2,2,N)
x, y = np.meshgrid(x, y)
z1 = gaus2d(x,y,1.0,1.0,0.1,0.2)
z2 = gaus2d(x,y,0.0,0.0,0.4,0.4)
z  = z1+0.25*z2
z  = z + np.random.randn(N,N)*0.00001
z  = np.maximum(z,1e-3)
np.savez('data/grid_matrix.npz',x=x,y=y,z=z)

N = 20*20
xrand = (np.random.rand(N)-0.5)*6
yrand = (np.random.rand(N)-0.5)*4
z1    = gaus2d(xrand,yrand,1.0,1.0,0.1,0.2)
z2    = gaus2d(xrand,yrand,0.0,0.0,0.4,0.4)
zrand = 1*z1+0.25*z2
zrand = zrand + np.random.randn(N)*0.001
zrand     = np.maximum(zrand,1e-3)
print(np.shape(zrand),np.shape(z),N)

np.savez('data/rand_matrix.npz',x=xrand,y=yrand,z=zrand)


"""
Crear datos de funciones Slepian DPSS
"""

import scipy.signal as signal

N = 100
x = np.linspace(0,N-1,N)
dpss, v = signal.windows.dpss(N, 4.0, 5, return_ratios=True)
dpss = dpss.T

fname = 'data/slepian.npz'
np.savez(fname,x=x,dpss=dpss,v=v)

