# plot_histogram.py
# A simple histogram examples

import matplotlib.pyplot as plt
import numpy as np


rd = np.random.RandomState()
X = rd.randn(10000)

fig, ax = plt.subplots()
ax.hist(X, bins=25, density=True)  # deprecated normed=True
x = np.linspace(-5, 5, 1000)
ax.plot(x, 1 / np.sqrt(2*np.pi) * np.exp(-(x**2)/2), linewidth=4)
ax.set_xticks([])
ax.set_yticks([])
plt.savefig('chap6_fig3.png')
plt.show() 
