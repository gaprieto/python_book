""" sphere_subs.py
    included in Package clase/
    /Dropbox/Dropbox/gprieto/python/Modules/clase

 SPHERE_SUBS is set of Python function definitions to compute distances
 and angles on a spherical Earth.  All angles are in degrees.
 Latitude used on standard maps is geographic latitude; this may be
 converted to the geocentric latitude used in these routines
 by using the SPH_GEOCENTRIC function.  Longitude input to
 these routines may be from either -180 to 180 or from 0 to 360.
 Longitude returned from these routines will be from 0 to 360.

 Based on Fortran subroutines from Peter M. Shearer

 Last Modified 
 German A. Prieto
 May 2017


 Contains definitions of
 sph_loc  - finds location of second point on sphere, given range 
            and azimuth at first point.
 sph_dist - computes angular separation of two points on sphere
 sph_azi  - computes distance and azimuth between two points 
            on the sphere
 sph_mid  - finds midpoint between two surface points on sphere
            and azimuth at midpoint to second point

"""

#--------------------------------------------------------------------
# sph_loc

def sph_loc(flat1,flon1,delta,azi):

   """ 
   SPH_LOC finds location of second point on sphere, given range 
   and azimuth at first point.

   Inputs:  flat1  =  latitude of first point (degrees) 
            flon1  =  longitude of first point (degrees)
            del    =  angular separation between points (degrees)
            azi    =  azimuth at 1st point to 2nd point, from N (deg.)
   Returns: flat2  =  latitude of second point (degrees)
            flon2  =  longitude of second point (degrees)
   """

   # import appropriate functions   
   import math  as mt
   import numpy as np

   if (delta == 0):
      flat2 = flat1
      flon2 = flon1
      return flat2, flon2

   raddeg = mt.pi/180.
   delr   = delta*raddeg
   azr    = azi*raddeg

   theta1=(90.-flat1)*raddeg
   phi1=flon1*raddeg   

   ctheta2 = mt.sin(delr)*mt.sin(theta1)*mt.cos(azr) + mt.cos(theta1)*mt.cos(delr)
   theta2  = mt.acos(ctheta2)

   if (theta1 == 0.): 
      phi2 = azr
   elif (theta2 == 0.):
      phi2=0.0
   else:
      sphi2 = mt.sin(delr)*mt.sin(azr)/mt.sin(theta2)
      cphi2 = (mt.cos(delr)-mt.cos(theta1)*ctheta2)/(mt.sin(theta1)*mt.sin(theta2))
      phi2 = phi1+mt.atan2(sphi2,cphi2)
      
   flat2=90.-theta2/raddeg
   flon2=phi2/raddeg
   
   if (flon2 > 360.):
      flon2=flon2-360.
   
   if (flon2 < 0.): 
      flon2=flon2+360.
   
   return flat2, flon2


# end sph_loc
#--------------------------------------------------------------------

#--------------------------------------------------------------------
# sph_dist

def sph_dist(flat1,flon1,flat2,flon2):

   """ 
   SPH_DIST computes angular separation of two points on sphere 
  
   Inputs:  flat1  =  latitude of first point (degrees)
            flon1  =  longitude of first point (degrees)
            flat2  =  latitude of second point (degrees)
            flon2  =  longitude of second point (degrees)
   Returns: delta  =  angular separation between points (degrees)
  
   Note: This routine is accurate depending on the precision of the 
   real numbers used. Python should be accurate to real(8) precision
   For greater accuracy, perform a separate calculation for close 
   ranges using Cartesian geometry.
   """

   # import appropriate functions   
   import math  as mt
   import numpy as np

   if ( (flat1 == flat2 and flon1 == flon2) 
   or (flat1 == 90. and flat2 == 90.) 
   or (flat1 == -90. and flat2 == -90.) ): 
      delta = 0.
      return [delta]

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

   return delta

# end sph_dist
#--------------------------------------------------------------------

#--------------------------------------------------------------------
# sph_azi

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

# end sph_azi
#--------------------------------------------------------------------

#--------------------------------------------------------------------
# sph_mid

def sph_mid(flat1,flon1,flat2,flon2):
   """
   SPH_MID finds midpoint between two surface points on sphere
   and azimuth at midpoint to second point
  
   Requires:  SPH_AZI, SPH_LOC
  
   Inputs:  flat1  =  latitude of first point (degrees) 
            flon1  =  longitude of first point (degrees)
            flat2  =  latitude of second point (degrees)
            flon2  =  longitude of second point (degrees)
   Returns: delta  =  angular separation between points (degrees)
            flat3  =  latitude of midpoint (degrees)
            flon3  =  longitude of midpoint (degrees)
            azi    =  azimuth at midpoint to first point

   calls sph_azi, sph_loc
   """ 

   delta,azi0   = sph_azi(flat1,flon1,flat2,flon2)

   del0         = delta/2.

   flat3,flon3  = sph_loc(flat1,flon1,del0,azi0)
   del2,azi     = sph_azi(flat3,flon3,flat2,flon2)

   return delta,flat3,flon3,azi
    
# end sph_mid
#--------------------------------------------------------------------
  

#c SPH_GEOCENTRIC converts Earth's geographic latitude to geocentric latitude
#c
#c  Inputs:  flat1  =  geographic latitude (degrees) 
#c                     (relative to local vertical)
#c  Returns: flat2  =  geocentric latitude (degrees)
#c                     (relative to Earth's center)
#c
#      subroutine SPH_GEOCENTRIC(flat1,flat2)
#      if (flat1.eq.90.) then
#         flat2=90.
#         return
#      end if
#      pi=3.141592654
#      degrad=180./pi
#      factor=0.9933056      !=(1-1/298.256)**2
#      phi=flat1/degrad
#      theta=atan(factor*tan(phi))
#      flat2=theta*degrad
#      return
#      end

#3
#
#c SPH_GEOGRAPHIC converts Earth's geocentric latitude to geographic latitude
#c
#c  Inputs:  flat1  =  geocentric latitude (degrees)
#c                     (relative to Earth's center)
#c  Returns: flat2  =  geographic latitude (degrees) 
#c                     (relative to local vertical)
#c
#      subroutine SPH_GEOGRAPHIC(flat1,flat2)
#      if (flat1.eq.90.) then
#         flat2=90.
#         return
#      end if
#      pi=3.141592654
#      degrad=180./pi
#      factor=0.9933056      !=(1-1/298.256)**2
#      theta=flat1/degrad
#      phi=atan(tan(theta)/factor)
#      flat2=phi*degrad
#      return
#      end
#
#
#c SPH_CART converts from spherical (lat,lon,r) to cartesian (x,y,z)
#c
#c Inputs:   flat  =  latitude (degrees)
#c           flon  =  longitude (degrees)
#c           r     =  radius
#c Returns:  x,y,z =  x,y,z coordinates (z=up)
#c
#      subroutine SPH_CART(flat,flon,r,x,y,z)
#      degrad=180./3.1415927
#      theta=(90.-flat)/degrad
#      phi=flon/degrad
#      stheta=sin(theta)
#      x=stheta*cos(phi)*r
#      y=stheta*sin(phi)*r
#      z=cos(theta)*r
#      return
#      end
#
#
#c SPH_SPH converts from cartesian (x,y,z) to spherical (lat,lon,r)
#c
#c Inputs:   x,y,z =  x,y,z coordinates (z=up)
#c Returns:  flat  =  latitude (degrees)
#c           flon  =  longitude (degrees)
#c           r     =  radius
#c
#      subroutine SPH_SPH(x,y,z,flat,flon,r)
#      degrad=180./3.1415927
#      r=sqrt(x*x+y*y+z*z)
#      if (r.eq.0.) then
#         flat=0.
#         flon=0.
#         return
#      end if
#      d=sqrt(x*x+y*y)
#      theta=atan2(d,z)
#      phi=atan2(y,x)
#      flat=90.-theta*degrad
#      flon=phi*degrad
#      if (flon.lt.0.) flon=flon+360.
#      return
#      end
#
#
#c SPH_POLE finds pole of great circle joining two points on sphere
#c
#c Requires:  SPH_CART, SPH_SPH
#c      
#c Inputs:  flat1  =  latitude of first point (degrees) 
#c          flon2  =  longitude of first point (degrees)
#c          flat2  =  latitude of second point (degrees)
#c          flon2  =  longitude of second point (degrees)
#c Returns: flat3  =  latitude of great circle pole (degrees)
#c          flon3  =  longitude of great circle pole (degrees)
#c
#      subroutine SPH_POLE(flat1,flon1,flat2,flon2,flat3,flon3)
#      call SPH_CART(flat1,flon1,1.,x1,y1,z1)
#      call SPH_CART(flat2,flon2,1.,x2,y2,z2)
#      x3=y1*z2-y2*z1
#      y3=x2*z1-x1*z2
#      z3=x1*y2-x2*y1
#      call SPH_SPH(x3,y3,z3,flat3,flon3,r)
#      return
#      end
#
#
#c SPH_TO_GCIRC rotates (lat,lon) to new coordinates using
#c specified great circle as new equator 
#c
#c Requires:  SPH_CART, SPH_SPH
#c
#c Inputs:   flat  =  latitude of point (degrees)
#c           flon  =  longitude of point (degrees)
#c           plat  =  latitude of great circle pole (degrees)
#c           plon  =  longitude of great circle pole (degrees)
#c Returns:  glat  =  latitude of point relative to great circle (degrees)
#c           glon  =  longitude of point relative to great circle (degrees)
#c
#      subroutine SPH_TO_GCIRC(flat,flon,plat,plon,glat,glon)
#      degrad=180./3.1415927
#      flon1=flon-plon
#      if (flon1.lt.0.) flon1=flon1+360.
#      call SPH_CART(flat,flon1,1.,x,y,z)
#      pcolat=90.-plat      
#      the=-pcolat/degrad
#      costhe=cos(the)
#      sinthe=sin(the)
#      yr=y
#      xr=costhe*x+sinthe*z
#      zr=costhe*z-sinthe*x
#      call SPH_SPH(xr,yr,zr,glat,glon,r)
#      return
#      end
#
#
#c SPH_FROM_GCIRC rotates (lat,lon) from great circle coordinates
#c back to original coordinates
#c
#c Requires:  SPH_CART, SPH_SPH
#c
#c Inputs:   glat  =  latitude of point relative to great circle (degrees)
#c           glon  =  longitude of point relative to great circle (degrees)
#c           plat  =  latitude of great circle pole (degrees)
#c           plon  =  longitude of great circle pole (degrees)
#c Returns:  flat  =  latitude of point (degrees)
#c           flon  =  longitude of point (degrees)
#c
#      subroutine SPH_FROM_GCIRC(glat,glon,plat,plon,flat,flon)
#      degrad=180./3.1415927
#      call SPH_CART(glat,glon,1.,xr,yr,zr)
#      pcolat=90.-plat
#      the=-pcolat/degrad
#      costhe=cos(the)
#      sinthe=sin(the)
#      y=yr
#      x=costhe*xr-sinthe*zr
#      z=costhe*zr+sinthe*xr
#      call SPH_SPH(x,y,z,flat,flon1,r)
#      flon=flon1+plon
#      if (flon.gt.360.) flon=flon-360.
#      return
#      end
