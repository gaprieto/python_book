"""
plot_errorbar.py
 Dada una tabla con valores de parámetros de fuente sísmica (Prieto et al., 2007)
 hacer una gráfica con barras de error. 
"""
import numpy as np
import matplotlib.pyplot as plt

# Cargar datos
fname = "data/source_error.dat"
data = np.loadtxt(fname,skiprows=1)
M0       = data[:,2]
M0_err   = data[:,3:5].T
fc       = data[:,5]
fc_err   = data[:,6:8].T
tau      = data[:,8]
tau_err  = data[:,9:11].T

# La figura
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,6))
ax1.errorbar(M0, fc,xerr=M0_err, yerr=fc_err,fmt='o')
ax1.set_ylim([1 , 100])
ax1.set_xlim(1e10, 1e15)
ax1.set_yscale('log')
ax1.set_xscale('log')
ax1.grid(which='both')
ax1.xaxis.tick_top()
ax1.xaxis.set_label_position("top")
ax1.set_xlabel('Seismic Moment (N.m)');
ax1.set_ylabel('Corner frequency (Hz)')

ax2.errorbar(M0, tau,xerr=M0_err, yerr=tau_err,fmt='^',color='black',
             ecolor='lightgray')
ax2.set_yscale('log')
ax2.set_xscale('log')
ax2.set_ylim([0.5 , 200])
ax2.set_xlim(1e10, 1e15)
#ax2.grid()
#ax2.yaxis.tick_right()
#ax2.yaxis.set_label_position("right")
ax2.set_xlabel('Seismic Moment (N.m)');
ax2.set_ylabel('Stress Drop (MPa)');
plt.savefig('../figs/chap07_fig3.pdf',bbox_inches='tight', pad_inches=0)
plt.show()

