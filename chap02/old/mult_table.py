# mult_table.py
# Genere una tabla de multiplicar para los números del 1 al 9

import numpy as np

i = np.arange(9)+1
j = np.arange(10)+1

for val1 in i:
    val2 = val1*j
    print ("Table of ", val1)
    print(val2)
   

