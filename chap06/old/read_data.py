# read_data.py
# Read a simple data file with numerical values

import numpy as np
import matplotlib.pyplot as plt

# Assign filename: file
file = 'some_data.dat'

# Import file: data
data = np.loadtxt(file)#, dtype='float')

# Plot results
plt.scatter(data[:, 0], data[:, 1])
plt.scatter(data[:, 0], data[:, 2])
plt.xlabel('Columna1')
plt.ylabel('Columnas 2, 3') 
plt.savefig('chap5_fig1.png') 
plt.show()


