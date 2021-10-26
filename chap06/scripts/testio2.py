"""
testio2.py
 Guarde y cargue varios arreglos en un único archivo 
 en formato NPZ de Numpy
"""
import numpy as np

m= 100000
n= 10
a = np.ones((m,n))*1.1
y = np.random.rand(n)
x = np.random.rand(m)
z = 1.5

print('Variables guardadas')
print('Shape de a, x, y, size(z)')
print(np.shape(a),np.shape(x),np.shape(y),np.size(z))
print('')

# Guardar en formato npz numpy
f1 = "dout/fout_testio2b.npz"
f2 = "dout/fout_testio2.npz"

np.savez(f1, a,x,y,m,n,z)
np.savez(f2, a=a,x=x,y=y,m=m,n=n,z=z)

# Cargar archivos, confirmar tamaños
npfile = np.load(f2)
n  = npfile.f.n
m  = npfile.f.m
x0 = npfile.f.x
y0 = npfile.f.y
a0 = npfile.f.a
z0 = npfile.f.z
print('Variables cargadas')
print('Shape de a, x, y, size(z)')
print(np.shape(a0),np.shape(x0),np.shape(y0),np.size(z0))
print('')

npfile2 = np.load(f1)
n1  = npfile2.f.arr_3
m1  = npfile2.f.arr_4
x1  = npfile2.f.arr_1
y1  = npfile2.f.arr_2
a1  = npfile2.f.arr_0
z1  = npfile2.f.arr_5
print('Variables cargadas 2')
print(npfile2.files)
print('Shape de a, x, y, size(z)')
print(np.shape(a1),np.shape(x1),np.shape(y1),np.size(z1))

