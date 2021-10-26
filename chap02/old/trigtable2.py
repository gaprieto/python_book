# trigtable2.py
# Create a simple trigonometric table (2)
#

from math import * 
import numpy as np

fmt = "%5.1f, %7.4f, %7.4f, %8.4f"

degrad = 180.0/pi

i = np.arange(90)

for ang in i :
   theta = float(ang)
   ctheta = cos(theta/degrad)
   stheta = sin(theta/degrad)
   ttheta = tan(theta/degrad)

   print (fmt %(theta,ctheta,stheta,ttheta))

