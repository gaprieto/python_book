# log_sqrt_table.py
# Code to run a table
# Begin with x = 1.01
#    at each step, multiply x by the integer loop, 
#    to create a new x
#    x = x*(i+1)
#
# At each step, calculate (and print) the 
#    log10, ln, and sqrt of x
#
# Make sure the table is organized. 


from math import *

x = 1.01
print('           x     log10        ln          sqrt')
print('----------------------------------------------')
for i in range(180):
   x = x*(i+1)
   l10 = log10(x)
   le  = log(x)
   sq  = sqrt(x)
   print ("%12.4e, %8.4f, %8.4f, %12.4e" % (x, l10, le, sq))
   if isinf(x):
      print('Loop ', i+1)
      break

