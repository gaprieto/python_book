"""
first_plot.py
   Gráfica usando objetos en Python
   de datos de Poli et al., 2016
"""

import numpy as np
import matplotlib.pyplot as plt

# load Poli data
fname = 'data/poli_2016.dat'
data = np.loadtxt(fname,usecols=[4,5,6])

fig = plt.figure()
ax  = fig.add_subplot(111)
ax.semilogy(data[:,0],data[:,1],'o')
plt.savefig('../figs/chap07_obj1.pdf',bbox_inches='tight', pad_inches=0)
plt.show()

