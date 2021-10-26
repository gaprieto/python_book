"""
primos.py
Programa para encontrar números primos hasta el 100
"""
import numpy as np

maxnum   = 100
prime    = np.zeros(maxnum)
prime[0] = 1

maxi = int(np.floor(np.sqrt(maxnum)))
for ipos in range(1,maxi):
    if (prime[ipos]==0):
        inum   = ipos+1
        maxj = int(np.floor(maxnum/inum)) 
        
        for j in range(2,maxj+1):
            imult = inum*j
            prime[imult-1] = 1

nprime = 0
for ipos in range(maxnum):
    if (prime[ipos]==0):
        nprime += 1
        print("%4i" %(ipos+1))
        
print ("# primos encontrados ", nprime)

