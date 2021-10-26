# prime.py
# Programa para calcular números primos hasta el 100

import numpy as np
import math as mt

maxnum = 1000

prod = np.zeros(maxnum)

#maxnum=100, max_i = 10
max_i = mt.floor(mt.sqrt(float(maxnum))) 

for i in range(2,max_i+1):
   if (prod[i-1]==0):   # for i-1 = 2
      max_j = mt.floor(maxnum/i)  # maxj = 50, maxj=33, etc.
      for j in range(2,max_j+1):
         prod[i*j-1] = 1    # 4, 6, 8, (-1)

nprime = 0   
for i in range(2,maxnum+1):
   if (prod[i-1]==0):
      nprime = nprime + 1
      print ("%4i" % i)

print ("Number of primes found ", nprime)


