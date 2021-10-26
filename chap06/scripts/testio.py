"""
testio.py
 Guardar y cargar una matrix grande 
 formatos binarios y ascii
"""
import numpy as np
import time

# tamaño de matriz
m= 100000
n= 10
a = np.ones((m,n))*1.1

# Guardar datos
f1 = 'dout/fout_testio.bin'
f2 = "dout/fout_testio.npy"
f3 = "dout/fout_testio.dat"
print('Tiempo requerido para guardar')

# formato binario
start = time.time()
a.tofile(f1)
print ('Binary: %8.5f segundos.' %(time.time()-start))

# formato Numpy nativo (binario)
start = time.time()
np.save(f2, a)
print ('Numpy:  %8.5f segundos.' %(time.time()-start))

# formato plano de texto
start = time.time()

np.savetxt(f3, a)
print ('text:   %8.5f segundos.' %(time.time()-start))

# Cargar datos
print('')
print('Tiempo requerido para cargar')

# formato binario
start = time.time()
b1 = np.fromfile(f1,dtype='float')
b1 = b1.reshape(m,n)
print ('Binary: %8.5f segundos.' %(time.time()-start))

# formato Numpy nativo (binario)
start = time.time()
b2 = np.load(f2)
print ('Numpy:  %8.5f segundos.' %(time.time()-start))

# formato plano de texto
start = time.time()
b3 = np.loadtxt(f3)
print ('text:   %8.5f segundos.' %(time.time()-start))


