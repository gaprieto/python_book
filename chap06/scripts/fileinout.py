# fileinout.py
# Lea un archivo con pares de números
# y guarde un archivo con el producto de los números
#
import numpy as np

fin  = 'data/another_data.dat'
fout = 'dout/test.dat'

# Cargar los datos, dos arreglos x y y
data = np.loadtxt(fin)
x = data[:,0][:,None] 
y = data[:,1][:,None]

# producto de los dos arreglos
z = x*y

# pegue arreglos en una sola matriz
M = np.hstack((x,y,z))

# Guarde un nuevo archivo, con formato
np.savetxt(fout, M,fmt='%8.4f %8.4f %8.4f')
#np.savetxt(fout, M,fmt="%15.10f")

print('Tamaño arreglos de entrada')
print(np.shape(x), np.shape(y))
print('Tamaño arreglo producto X*Y')
print(np.shape(z))
print('Tamaño arreglo de salida')
print(np.shape(M))


