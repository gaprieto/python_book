# usersqrt.py
# Ask user for number and take sqrt. 

from math import *   # import math functions

for i in range(5):
   x = float(input("Enter positive real number: "))
   if (x==0.0):
      break
   elif (x<0.0):
      print("Number is negative")
      continue
   else:
      y = sqrt(x)
   
   print ('sqrt = ',y)
   


