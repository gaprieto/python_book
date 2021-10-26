#
# Gráfica de una serie de Fourier for boxcar
#

import numpy as np
import matplotlib.pyplot as plt

# Create X vector
pi = np.pi
x = np.linspace(-pi,pi,101)

# Exact boxcar
f = np.ones(len(x))
iloc = np.argwhere(x<0)
f[iloc] = -1

# Different odd terms of sin function
s01 = np.sin(x)
s03 = np.sin(3*x)/3.
s05 = np.sin(5*x)/5.
s07 = np.sin(7*x)/7.
s09 = np.sin(9*x)/9.
s11 = np.sin(11*x)/11.

# Function of Fourier series
y1 = (4/pi)* (s01+s03)
y2 = (4/pi)* (s01+s03+s05+s07)
y3 = (4/pi)* (s01+s03+s05+s07+s09+s11)


# Plot
fig = plt.figure()
plt.plot(x,f,'b-'  ,lw=3,label='Boxcar')
plt.plot(x,y1,'c--',lw=2,label='2 terms')
plt.plot(x,y2,'r-' ,lw=2,label='4 terms')
plt.plot(x,y3,'b:' ,lw=2,label='6 terms')

plt.title(r'$\sum_{i=1}^{N} \frac{sin(i*x)}{i}$ for $i$ odd')
plt.xlabel('X')
plt.ylabel('Fouriewr series sum')
plt.legend()
plt.savefig('chap6_fig7b.png')
plt.show()

