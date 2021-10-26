"""
cartomap03.py
 Mapa Suramérica con limites políticos
"""
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature

reg  = [-85, -30, -60, 15]
proj = ccrs.PlateCarree() 

fig = plt.figure(figsize=(10,8))
ax  = fig.add_subplot(111,projection=proj)
ax.set_extent(reg)
ax.coastlines()
ax.add_feature(cfeature.BORDERS,linestyle=':')

plt.savefig('../figs/chap08_map03.pdf',bbox_inches='tight', pad_inches=0)
plt.show()

