# testio2.py
# Save (and load) a large matrix in 
# Binary or ascii format

import numpy as np
import time

m= 100000
n= 10
a = np.ones((m,n))*1.1
y = np.random.rand(n)
x = np.random.rand(m)

# Save in Native Numpy format
start = time.time()
np.savez("fout_testio2b.npz", a,x,y,m,n)
np.savez("fout_testio2.npz", a=a,x=x,y=y,m=m,n=n)
print ('Numpy  save time ', time.time()-start, 'seconds.')

# Load the file and look at arrays
start = time.time()
npzfile = np.load("fout_testio2.npz")
print ('Numpy  load time ', time.time()-start, 'seconds.')

n  = npzfile.f.n
m  = npzfile.f.m
x0 = npzfile.f.x
y0 = npzfile.f.y
a0 = npzfile.f.a

print(m,n)
print(y0)
print(npzfile.files)

npzfile = np.load("fout_testio2b.npz")
print(npzfile.files)

