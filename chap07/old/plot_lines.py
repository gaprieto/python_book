# plot_lines.py
# Example of simple line plotting

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10., 10., num=20)


y1 = x*0 + 1
y2 = 0.2*x + 0.1
y3 = 0.05*x**2 + 0.1*x - 0.1
y4 = -0.002*x**3 + 0.01*x**2 - 0.05*x + 0.1
y5 = +1e-4*x**4 +0.002*x**3 + 0.01*x**2 - 0.05*x + 0.1

plt.plot(x,y1,marker='^',linestyle=' ',label='y1')
plt.plot(x,y2,':',label='y2')
plt.plot(x,y3,'--',label='y3')
plt.plot(x,y4,'-.',label='y4')
plt.plot(x,y5,'-',label='y5')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('X vs Y')
plt.ylim((-3, 8))
plt.legend()
plt.savefig('chap6_fig1.png')
plt.show()

