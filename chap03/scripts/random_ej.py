"""
random_ej.py
Genere números aleatorios, float y enteros
"""

import numpy as np

for i in range(5):
    a = np.random.random() # dist uniforme
    b = np.random.randint(1,10)
    print ("%8.7f %2i"%(a,b))

