"""
plot_scatter.py
"""
import matplotlib.colors as cm
import matplotlib.pyplot as plt
import numpy as np

fdat = np.load("data/rand_matrix.npz")
x = fdat.f.x
y = fdat.f.y
z = fdat.f.z

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,8))
im1 = ax1.scatter(x,y,z*40+15,c=z,cmap='terrain',edgecolor='gray')
ax1.set_xticks([])
plt.colorbar(im1,ax=ax1)
ax1.set_title('Linear color scale')

im2 = ax2.scatter(x,y,z*40+15,c=z,norm=cm.LogNorm(), cmap='terrain',edgecolor='k')
ax2.set_title('Log color scale')
plt.colorbar(im2,ax=ax2)
plt.savefig('../figs/chap07_fig5.pdf',bbox_inches='tight', pad_inches=0)
plt.show()

fig2 = plt.figure(figsize=(8,8))
ax = fig2.add_subplot(111, projection='3d')
ax.plot_trisurf(x,y,np.log10(z))
ax.set_title('Tri-Surf log10(Z)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('log(Z)')
ax.view_init(45, 135)
plt.savefig('../figs/chap07_fig6.pdf',bbox_inches='tight', pad_inches=0)

plt.show()

