"""
plot_mandel.py
"""
import numpy as np
import matplotlib.pyplot as plt
import mandel as md

# Graficar
x0 =-0.21503361460851339
y0 = 0.67999116792639069
dx = 0.4

fig = plt.figure(figsize=(10,10))
dat = md.mandel1(x0,y0,dx)
nx = np.shape(dat)[0]
ax = fig.add_subplot(1,1,1)
im = ax.imshow(dat,cmap='twilight_shifted',animated=True)
ax.set_title(f'Escala: {2*dx:.1e}')
ax.set_xticks([])
ax.set_yticks([])
plt.show()

