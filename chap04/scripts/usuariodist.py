# usuariodist.py
# Program para calcular la distancia y azimut entre dos
# puntos sobre una esfera. 

def sph_azi(flat1,flon1,flat2,flon2):
   """ 
   SPH_AZI computes distance and azimuth between two points 
   on the sphere
   
   Inputs: flat1 = latitude of first point (degrees)
           flon2 = longitude of first point (degrees)
           flat2 = latitude of second point (degrees)
           flon2 = longitude of second point (degrees)
    
   Returns: del = angular separation between points (degrees)
            azi = azimuth at 1st point to 2nd point, from N (deg.)
   
   Notes:
   (1) applies to geocentric not geographic lat,lon on Earth
   
   (2) This routine is accurate depending on the precision of the 
   real numbers used. Python should be accurate to real(8) precision
   For greater accuracy, perform a separate calculation for close 
   ranges using Cartesian geometry.
   """

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

   raddeg=np.pi/180.

   theta1=(90.-flat1)*raddeg
   theta2=(90.-flat2)*raddeg

   phi1=flon1*raddeg
   phi2=flon2*raddeg
   
   stheta1=np.sin(theta1)
   stheta2=np.sin(theta2)
   ctheta1=np.cos(theta1)
   ctheta2=np.cos(theta2)

   cang=stheta1*stheta2*np.cos(phi2-phi1)+ctheta1*ctheta2
   ang=np.arccos(cang)
   delta=ang/raddeg

   sang=np.sqrt(1.-cang*cang)
   caz=(ctheta2-ctheta1*cang)/(sang*stheta1)
   saz=-stheta2*np.sin(phi1-phi2)/sang
   az=np.arctan2(saz,caz)
   azi=az/raddeg

   if (azi < 0.): 
      azi=azi+360.

   return [delta, azi]

#------------------------------------------------
# Programa principal
#------------------------------------------------

lat1 = None 
lon1 = None
lat2 = None
lon2 = None
while (lat1!=0. or lon1!=0. or lat2!=0. or lon2!=0.):
    intxt = input('Enter 1st point lat/lon ')
    lat1,lon1 = intxt.split()
    lat1 = float(lat1)
    lon1 = float(lon1)
    
    intxt = input('Enter 2nd point lat/lon ')
    lat2,lon2 = intxt.split()
    lat2 = float(lat2)
    lon2 = float(lon2)
    
    delta,azi = sph_azi(lat1,lon1,lat2,lon2)
    print('Distancia y acimut:  %6.2f  %7.2f '%(delta, azi))
    
# Bogota - New York    
# 4.60 -74.08
# 40.71 -74.00
# Distancia y acimut:   36.11     0.10 

# Bogota - Paris
# 4.60 -74.08
# 48.85 2.35
# Distancia y acimut:   77.63    40.91 

# Bogota - Buenos Aires
# 4.60 -74.08
# -34.60 -58.37
# Distancia y acimut:   41.90   160.50 

