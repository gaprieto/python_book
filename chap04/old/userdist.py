# userdist.py
# Program to calculate the distance and azimuth of two points 
# on the surface of the Earth. 

def sph_azi(flat1,flon1,flat2,flon2):
   # SPH_AZI computes distance and azimuth between two points 
   # on the sphere
   #
   # Inputs: flat1 = latitude of first point (degrees)
   #         flon2 = longitude of first point (degrees)
   #         flat2 = latitude of second point (degrees)
   #         flon2 = longitude of second point (degrees)
   # 
   # Returns: del = angular separation between points (degrees)
   #          azi = azimuth at 1st point to 2nd point, from N (deg.)
   #
   # Notes:
   # (1) applies to geocentric not geographic lat,lon on Earth
   #
   # (2) This routine is accurate depending on the precision of the 
   # real numbers used. Python should be accurate to real(8) precision
   # For greater accuracy, perform a separate calculation for close 
   # ranges using Cartesian geometry.
   #

   # import appropriate functions   
   import math  as mt
   import numpy as np
   
   if ( (flat1 == flat2 and flon1 == flon2) 
   or (flat1 == 90. and flat2 == 90.) 
   or (flat1 == -90. and flat2 == -90.) ): 
      delta = 0.
      azi = 0.
      return [delta,azi]

   # Perform calculation
   delta = 0.
   azi   = 0.

   raddeg=mt.pi/180.

   theta1=(90.-flat1)*raddeg
   theta2=(90.-flat2)*raddeg

   phi1=flon1*raddeg
   phi2=flon2*raddeg
   
   stheta1=mt.sin(theta1)
   stheta2=mt.sin(theta2)
   ctheta1=mt.cos(theta1)
   ctheta2=mt.cos(theta2)

   cang=stheta1*stheta2*mt.cos(phi2-phi1)+ctheta1*ctheta2
   ang=mt.acos(cang)
   delta=ang/raddeg

   sang=mt.sqrt(1.-cang*cang)
   caz=(ctheta2-ctheta1*cang)/(sang*stheta1)
   saz=-stheta2*mt.sin(phi1-phi2)/sang
   az=mt.atan2(saz,caz)
   azi=az/raddeg

   if (azi < 0.): 
      azi=azi+360.

   return [delta, azi]

#------------------------------------------------
# Start main code
#------------------------------------------------

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

   delta,azi = sph_azi(lat1,lon1,lat2,lon2)

   print ("del, azi =, ", delta,azi)
