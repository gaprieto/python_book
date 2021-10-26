"""
naive_plot.py
   Gráfica usando plt.plot()
   de datos de Poli et al., 2016
"""
import numpy as np
import matplotlib.pyplot as plt

# load Poli data
fname = 'data/poli_2016.dat'
data = np.loadtxt(fname,usecols=[4,5,6])


plt.semilogy(data[:,0],data[:,1],'o')
plt.savefig('../figs/chap07_fig1.pdf',bbox_inches='tight', pad_inches=0)
plt.show()

