# prime2.py
# Program to calculate prime numbers
# A matrix with up to 200 prime numbers will we printed. 

import numpy as np
import math as mt

maxnum = 2000

prod = np.zeros(maxnum)
pnum = np.zeros(200)
  
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
      pnum[nprime-1] = i 
   if (nprime==200):
      break

print ("Number of primes found ", nprime)

a = pnum.reshape(20, 10)

print (a)

