# prob_c5_1.py

import numpy as np

fin  = input("Enter input file name ")

fout = input("Enter output file name ")
 
# Load data and extract shape
data = np.loadtxt(fin)
nrow, ncol = data.shape

# Demean data
for i in range(nrow):
   data[i,:] = data[i,:]-np.mean(data[i,:])

# Save data with given format
np.savetxt(fout, data,fmt='%5.2f')

