"""
four_subplots.py
 Programa para iniciar 4 subplots en una sola figura
 subplots 2 y 3 con datos de Poli et al., 2016
"""
import numpy as np
import matplotlib.pyplot as plt

# load Poli data
fname = 'data/poli_2016.dat'
data = np.loadtxt(fname,usecols=[4,5,6])

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 5))
ax2.semilogy(data[:,0],data[:,1],'ko')
ax3.semilogy(data[:,0],data[:,2],'r^')

plt.savefig('../figs/chap07_obj3.pdf',bbox_inches='tight', pad_inches=0)
plt.show()

