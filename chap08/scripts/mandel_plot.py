# mandel_plot.py
# Plot the mandelbrot set for a number of points
#
import numpy as np
import matplotlib.pyplot as plt
import mandel as md
    
# cree la figura
fig = plt.figure(figsize=(8,10))
# Defina los límites X,Y 
x1,x2 = -2, 2 
y1,y2 = -2, 2
ax  = fig.add_subplot(3,2,(1,2))
md.mandel(ax,x1,x2,y1,y2)

x1,x2 = -2, 0.5 
y1,y2 = -0.5, 2
ax.plot([x1, x2, x2, x1, x1],[y1, y1, y2, y2, y1],'k')
ax  = fig.add_subplot(3,2,3)
md.mandel(ax,x1,x2,y1,y2)

x1,x2 = -1.5, -0.5 
y1,y2 = -0.2, 0.5
ax.plot([x1, x2, x2, x1, x1],[y1, y1, y2, y2, y1],'k')
ax  = fig.add_subplot(3,2,4)
md.mandel(ax,x1,x2,y1,y2)

x1,x2 = -1.45, -1.2 
y1,y2 = -0.04, 0.08
ax.plot([x1, x2, x2, x1, x1],[y1, y1, y2, y2, y1],'k')
ax  = fig.add_subplot(3,2,5)
md.mandel(ax,x1,x2,y1,y2)

x1,x2 = -1.405, -1.384 
y1,y2 = -0.0025, 0.005
ax.plot([x1, x2, x2, x1, x1],[y1, y1, y2, y2, y1],'k')
ax  = fig.add_subplot(3,2,6)
md.mandel(ax,x1,x2,y1,y2)

plt.savefig('../../figs/chap08_fig1.pdf',
            bbox_inches='tight', pad_inches=0)
plt.show()       


