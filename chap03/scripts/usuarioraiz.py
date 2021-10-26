# usuarioraiz.py
# Solicite al usuario un número real y toma la raíz cuadrada.
#

import numpy as np

x = None
while (x!=0.0):
    x = float(input("Digite un número real y positivo: "))
    if (x<0.0):
        print('Número es negativo')
        continue
    else:
        y = np.sqrt(x)
    print ('sqrt(',x,') = ',y)
    

