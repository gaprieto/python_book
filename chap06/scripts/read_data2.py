"""
read_data2.py
 Leer un archivo plano con datos numéricos en columnas. 
"""
import numpy as np
import matplotlib.pyplot as plt

# nombre del archivo
fname = 'data/some_data_header.dat'

# Cargar archivo: data
data = np.loadtxt(fname, skiprows=1)

# Figura
plt.scatter(data[:, 0], data[:, 2]/data[:,1])
plt.ylim([-30, 30])
plt.savefig('../figs/chap06_fig2.pdf',bbox_inches='tight', pad_inches=0)
plt.show()

