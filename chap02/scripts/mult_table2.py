# mult_table2.py
# Genere la tabla de multiplicar del 7. 

import numpy as np

x = 7                          # la tabla del 7
i = np.arange(10)

for y in i:            # loop 0, 1, 2, ..., 9
    z = x*y
    print(x,'x',y,' = ',z)

