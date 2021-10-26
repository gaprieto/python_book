# array2fun.py
import numpy as np
import arr_subs as arr

mu    = 25
sigma = 3.0 
a = np.random.normal(mu,sigma,5)
n = np.size(a)
print('Arreglo original ')
print (a)

[b,x_mean,x_var] = arr.arr_trab(a)

print('Arreglo corregido (demeaned)')
print(b)

print("Prom(x) = ",x_mean)
print("Var(x)  = ",x_var)

