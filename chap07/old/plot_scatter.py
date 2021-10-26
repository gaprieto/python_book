# plot_scatter.py

import matplotlib.colors as cm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as ml

N = 2000
x = (np.random.rand(N)-0.5)*6
y = (np.random.rand(N)-0.5)*4

z = (ml.bivariate_normal(x, y, 0.1, 0.2, 1.0, 1.0)
     + 0.5 * ml.bivariate_normal(x, y, 0.5, 0.5, 0.0, 0.0))

z = z+1e-5

plt.subplot(212)
plt.scatter(x, y, c=z, norm=cm.LogNorm(), cmap='winter')
plt.colorbar()
plt.title('Log color scale')

plt.subplot(211)
plt.scatter(x, y, c=z, cmap='winter')
plt.colorbar()
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([])
plt.title('Linear color scale')

plt.savefig('chap6_fig4.png')
plt.show()

