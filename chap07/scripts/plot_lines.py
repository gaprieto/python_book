"""
plot_lines.py
 Ejemplo de varias formas de graficar arreglos
"""
import numpy as np
import matplotlib.pyplot as plt

fdat = np.load('data/slepian.npz')
x    = fdat.f.x
dpss = fdat.f.dpss
v    = fdat.f.v

fig,ax = plt.subplots(figsize=(8,7))
ax.plot(x,dpss[:,0],marker='^',linestyle=' ',label=v[0])
ax.plot(x,dpss[:,1],":",label=v[1])
ax.plot(x,dpss[:,2],"--",label=v[2])
ax.plot(x,dpss[:,3],marker='.',label=v[3])
ax.plot(x,dpss[:,4],'-s',label=v[4])

ax.set_xlabel('tiempo')
ax.set_ylabel('Amplitud')
ax.set_title('Funciones Slepian y su concentración')
ax.set_ylim((-0.22, 0.22))
ax.legend()
plt.savefig('../figs/chap07_fig2.pdf',bbox_inches='tight', pad_inches=0)

# mejora la gráfica
#
fig = plt.figure(figsize=(7,6))
ax  = fig.add_subplot(111)
ax.plot(x,dpss[:,0],marker='^',linestyle=' ',label=r'$\lambda_0$=%11.9f '%(v[0]))
ax.plot(x,dpss[:,1],':',label=r'$\lambda_1$=%11.9f '%(v[1]))
ax.plot(x,dpss[:,2],'--',label=r'$\lambda_2$=%11.9f '%(v[2]))
ax.plot(x,dpss[:,3],'-.',label=r'$\lambda_3$=%11.9f '%(v[3]))
ax.plot(x,dpss[:,4],'-',label=r'$\lambda_4$=%11.9f '%(v[4]))

ax.set_xlabel('tiempo')
ax.set_ylabel('Amplitud')

ax.set_title('Funciones Slepian y su concentración')
ax.set_ylim((-0.22, 0.22))
ax.legend()
plt.show()

