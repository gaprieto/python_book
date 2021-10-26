"""
plot_histogram.py
 Figura de esfuerzos asociados a terremotos profundos
 Piero et al., 2016
"""

import matplotlib.pyplot as plt
import numpy as np

# load Poli data
fname = 'data/poli_2016.dat'
data  = np.loadtxt(fname,usecols=[5,6])

bins=np.linspace(5,8.5,20)
labels = [0.1, 1.0,10, 100]

fig, ax = plt.subplots()
ax.hist(np.log10(data[:,0]),bins=10,label='Stress Drop')
ax.hist(np.log10(data[:,1]),bins=bins,label='Apparent Stress')

ax.set_xlim(5, 8)
ax.set_xticks((5,6,7,8))
ax.set_xticklabels(labels)
ax.set_xlabel('Stress Drop/Apparent Stress (MPa)')
ax.set_ylabel('Count')
ax.set_yticks([])
plt.legend()
plt.savefig('../figs/chap07_fig4.pdf',bbox_inches='tight', pad_inches=0)
plt.show()

