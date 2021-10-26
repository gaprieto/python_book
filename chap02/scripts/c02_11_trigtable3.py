# trigtable3.py
# Genera una tabla trigonométrica simple. 
# Imprima los resultados para cos, sin, tan.
#    Ahora, imprima los resultados con mejor presentación
#    Defina el formato desde el comienzo
#

from math import *
import numpy as np

fmt = "%5.1f, %7.4f, %7.4f, %8.4f"    # definir formato al comienzo

i = np.arange(90)

for ang in i :
    theta = float(ang/180.*pi)
    ctheta = cos(theta)
    stheta = sin(theta)
    ttheta = tan(theta)
    
    print(fmt % (ang,ctheta,stheta,ttheta))


