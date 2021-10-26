# plot_contour.py

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as cm
import matplotlib.pyplot as plt
import numpy as np

fdat = np.load("data/grid_matrix.npz")
x = fdat.f.x
y = fdat.f.y
z = fdat.f.z

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,8))
im1 = ax1.contour(x,y,z,[1e-3, 1e-2,1e-1,1e0,1e1],
                  colors='k')
ax1.clabel(im1,inline=1,fontsize=8,fmt="%4.0e")
ax1.set_xticks([])
fig.colorbar(im1,ax=ax1)
fig.delaxes(fig.axes[2])
ax1.set_title('Contour plot')

im2 = ax2.contourf(x, y, z,norm=cm.LogNorm(),cmap='ocean')
fig.colorbar(im2,ax=ax2)
ax2.set_title('Contour filled')
plt.savefig('../figs/chap07_fig7.pdf',bbox_inches='tight', pad_inches=0)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, np.log10(z),cmap='ocean')
plt.title('Surface log10(Z)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('log(Z)')
ax.view_init(45, 135)
plt.savefig('../figs/chap07_fig8.pdf',bbox_inches='tight', pad_inches=0)

plt.show()
