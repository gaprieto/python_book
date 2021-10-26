# pres_tierra.py
# Calcule la presión en el interior de la 
# Tierra, a diferentes profundidades. 
# Asuma presión hidrostática para la corteza, 
# densidad del granito, y que g (acc gravedad) es
# constante.
#

import numpy as np

fmt = "%5.1f %14.1f "
g   = 9.8    # m/s2
rho = 2700.0 # kg/m3

print('Prof.  Presión (MPa)')
for i in range(11):
   h = float(i)*5*1000  # depth(m)
   P = g*rho*h        # Pascal
   PMpa = P/1e6      # MPa
   print(fmt %(h/1000 ,PMpa))


