# trigtable2.py
# Genera una tabla trigonométrica simple. 
# Imprima los resultados para cos, sin, tan.
#    Ahora, imprima los resultados con mejor presentación
#


import math
import numpy as np

i = np.arange(90)

for ang in i :
    theta = float(ang/180.*math.pi)
    ctheta = math.cos(theta)
    stheta = math.sin(theta)
    ttheta = math.tan(theta)
    
    # Desplegar resultados más amables
    print ("%5.1f, %7.4f, %7.4f, %8.4f"
           % (ang,ctheta,stheta,ttheta))


