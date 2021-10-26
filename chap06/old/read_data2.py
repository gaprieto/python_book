# read_data2.py
# Read a simple data file with numerical values
# and a header

import numpy as np
import matplotlib.pyplot as plt

# Assign filename: file
file = 'some_data_header.dat'

# Import file: data
data = np.loadtxt(file, skiprows=1)

# Plot results
plt.scatter(data[:, 0], data[:, 2]/data[:,1])
plt.ylim(-75, 75)
plt.ylabel('Columna 3/Columna 2')
plt.xlabel('Columna 1')
plt.savefig('chap5_fig2.png') 
plt.show()


