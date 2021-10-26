# fileinout.py
# Read a simple text file with a pair of numbers
# and output their product in a new file

import numpy as np

fin = input("Enter input file name ")

# Load data and put in individual arrays
data = np.loadtxt(fin)
x = data[:,0]
y = data[:,1]

fout = input("Enter output file name ")

# Product of two arrays
z = x*y

# Put all arrays together, and vertical
data_out = np.vstack((x,y,z)).T

# Save data with given format
np.savetxt(fout, data_out,fmt='%5.2f %5.2f %5.2f')

