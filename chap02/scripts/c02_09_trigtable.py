# trigtable.py
# Genera una tabla trigonométrica simple. 
# Imprima los resultados para cos, sin, tan.
#

import math
import numpy as np

i = np.arange(90)

for ang in i :
    theta = float(ang/180.*math.pi)
    ctheta = math.cos(theta)
    stheta = math.sin(theta)
    ttheta = math.tan(theta)
    
    print (ang,ctheta,stheta,ttheta)


