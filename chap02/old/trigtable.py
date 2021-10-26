# trigtable.py
# Create a simple trigonometric table
#

import math
import numpy as np

degrad = 180.0/3.1415927

i = np.arange(90)

for ang in i :
   theta = float(ang)
   ctheta = math.cos(theta/degrad)
   stheta = math.sin(theta/degrad)
   ttheta = math.tan(theta/degrad)

   print ("%5.1f, %7.4f, %7.4f, %8.4f"
          % (theta,ctheta,stheta,ttheta))

