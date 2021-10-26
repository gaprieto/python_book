"""
plot_mandel_array.py
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import mandel as md

# Zoom factor
zfac = 5.0

# Graficar
x0 =-0.21503361460851339
y0 = 0.67999116792639069
dx = 0.4

fig = plt.figure(figsize=(10,10))
for i in range(9):
    dat = md.mandel1(x0,y0,dx)
    nx = np.shape(dat)[0]
    ax = fig.add_subplot(3,3,i+1)
    im = ax.imshow(dat,cmap='twilight_shifted',animated=True)
    ax.set_title(f'Escala: {2*dx:.1e}')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.text(14,28,i+1,color='white',
           fontsize = 16, fontweight ='bold')
    dx  = dx/zfac
    fac = (nx/2)/zfac     
    if (i==8):
        continue
    xbx = np.array([-fac,+fac,+fac,-fac,-fac])+nx/2
    ybx = np.array([-fac,-fac,+fac,+fac,-fac])+nx/2
    ax.plot(xbx,ybx,'r-')
 
plt.savefig('../figs/chap09_fig1.pdf',bbox_inches='tight', pad_inches=0)
plt.show()

