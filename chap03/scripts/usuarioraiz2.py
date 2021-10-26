# usuarioraiz2.py
# Solicite al usuario un número real y toma la raíz cuadrada.
#

import numpy as np

for i in range(5):
    x = float(input("Digite un número real y positivo: "))
    if (x<0.0):
        print('Número es negativo')
        continue
    elif (x==0.0):
        break
    else:
        y = np.sqrt(x)
    print ('sqrt(',x,') = ',y)
    

