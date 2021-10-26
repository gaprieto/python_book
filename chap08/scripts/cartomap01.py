"""
cartomap01.py
 Mapa global general
"""
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# Proyección PlateCaree 
proj0 = ccrs.PlateCarree(central_longitude=180.0)

fig = plt.figure(figsize=(10,8))
ax  = fig.add_subplot(projection=proj0)
ax.coastlines()
ax.set_xticks([-180, -120, -60, 0, 60, 120, 180], crs=proj0)
ax.set_yticks([-90, -60, -30, 0, 30, 60, 90], crs=proj0)
               
plt.savefig('../figs/chap08_map01.pdf',bbox_inches='tight', pad_inches=0)
plt.show()

