# userdist2.py
# Program to calculate the distance and azimuth of two points 
# on the surface of the Earth. 

import clase.sphere_subs as sphere 


for i in range(10):
   intxt = input("Enter 1st point lat, lon ")
   lat1,lon1 = intxt.split()
   lat1 = float(lat1)
   lon1 = float(lon1)

   intxt = input("Enter 2nd point lat, lon ")
   lat2,lon2 = intxt.split()
   lat2 = float(lat2)
   lon2 = float(lon2)

   if (lat1==0 and lon1==0 and lat2==0 and lon2==0):
      break

   delta,azi = sphere.sph_azi(lat1,lon1,lat2,lon2)

   print ("del, azi =, ", delta,azi)
