# plot_errorbar.py
# Simple code to plot some data with 
# error bars, and synthetic curve

import numpy as np
import matplotlib.pyplot as plt

N    = 20
x    = np.random.rand(N)*4
x    = np.sort(x)
sig  = 0.01 + 0.1*np.sqrt(x)
yerr = np.random.normal(0,0.3,size=N)*sig 
y    = np.exp(-x) + yerr

x0 = np.linspace(0.0, 4.0)
y0   = np.exp(-x0)

# Plot the data

f, axs = plt.subplots(1, 2)

ax1 = axs[0]
ax1.scatter(x, y)
ax1.plot(x0,y0,color='r')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_ylim([-0.2 , 1.1])

ax2 = axs[1]
ax2.errorbar(x, y,yerr=sig,fmt='o')
ax2.plot(x0,y0,color='r')
ax2.set_xlabel('X')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
ax2.set_ylabel('Y')
ax2.set_ylim([-0.2 , 1.1])

plt.savefig('chap6_fig2.png')
plt.show() 

