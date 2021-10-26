# plot_contour.py

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as cm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as ml

delta = 0.025
x     = np.arange(-3.0, 3.0,delta)
y     = np.arange(-2.0, 2.0, delta)
X, Y  = np.meshgrid(x,y)


z = (ml.bivariate_normal(X, Y, 0.1, 0.2, 1.0, 1.0)
     + 0.5 * ml.bivariate_normal(X, Y, 0.5, 0.5, 0.0, 0.0))
z = z+1e-5

plt.figure(1)
plt.subplot(212)
CS = plt.contourf(X, Y, z,norm=cm.LogNorm())
plt.colorbar()
plt.title('Contour filled')

plt.subplot(211)
CS = plt.contour(X, Y, z,norm=cm.LogNorm(),colors='k')
plt.clabel(CS,inline=1,fontsize=10,fmt='%4.1e')
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([])
plt.colorbar()
plt.title('Log Contour plot')
plt.savefig('chap6_fig5.png')
plt.show()

fig  = plt.figure()
ax   = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, np.log10(z),cmap='terrain')
plt.title('Surface log10(Z)')

plt.savefig('chap6_fig6.png')
plt.show()

