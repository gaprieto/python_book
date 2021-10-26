"""
read_data.py
 Leer un archivo plano con datos numéricos en columnas. 
"""

import numpy as np
import matplotlib.pyplot as plt

# nombre del archivo
fname = 'data/some_data.dat'

# Cargue el archivo con Numpy
data = np.loadtxt(fname)

# Figura de columnas 1 vs 2, 1, vs 3
plt.scatter(data[:, 0], data[:, 1])
plt.scatter(data[:, 0], data[:, 2])
plt.savefig('../figs/chap06_fig1.pdf',bbox_inches='tight', pad_inches=0)
plt.show()


