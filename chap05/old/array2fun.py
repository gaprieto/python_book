# array2fun.py
# Program showing working with arrays in functions

def arr_work(x,n):
   # Function to do some basic analysis of an array of size n
   # Input: x     = array of given size, with numbers
   #        n     = size of the array
   # Output y     = demeaned array
   #        y_var = variance of array

   import numpy as np


   if (np.size(x) != n):
      print("problem with size")
      return -1,-1,-1

   x_mean = np.mean(x)
   y = x-x_mean
   y_var = np.var(y)

   return [y,x_mean,y_var]

#--------------------
# Main program

import numpy as np

a = np.random.rand(5)
n = np.size(a)

print (a)

[b,x_mean,x_var] = arr_work(a,n)

print(b)
print("Mean(x) = ",x_mean)
print("Var(x)  = ",x_var)

