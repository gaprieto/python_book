# hyp_fun.py
# Hacer una tabla con cosh, senh
# desde 0.0 hasta 6.0, cada 0.5

from math import *

print ("   x      sinh      cosh")
print ("------------------------")
for i in range(13):
   x = float(i)*0.5
   chyp = cosh(x)
   shyp = sinh(x)

   print ("%4.1f, %8.4f, %8.4f" % (x,shyp, chyp))

