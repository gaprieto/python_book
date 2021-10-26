# testio.py
# Save (and load) a large matrix in 
# Binary or ascii format

import numpy as np
import time

m= 100000
n= 10
a = np.ones((m,n))*1.1

# save file in binary format
start = time.time()
a.tofile("fout_testio.bin")
print ('Binary save time ', time.time()-start, 'seconds.')

# Save in Native Numpy format
start = time.time()
np.save("fout_testio.npy", a)
print ('Numpy  save time ', time.time()-start, 'seconds.')

# save file in plain text
start = time.time()
fout = "fout_testio.dat"
np.savetxt(fout, a)
print ('text   save time ', time.time()-start, 'seconds.')


#
# Loading those files again
#

print(" ")
# save file in binary format
start = time.time()
b1 = np.fromfile("fout_testio.bin",dtype='float')
b1 = b1.reshape(m,n)
print ('Binary load time ', time.time()-start, 'seconds.')

# Save in Native Numpy format
start = time.time()
b2 = np.load("fout_testio.npy")
print ('Numpy  load time ', time.time()-start, 'seconds.')

# save file in plain text
start = time.time()
b3 = np.loadtxt("fout_testio.dat")
print ('text   load time ', time.time()-start, 'seconds.')

print(b1.shape)
print(b2.shape)
print(b3.shape)



