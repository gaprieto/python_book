"""
cartomap06.py
 Con topo, y estaciones lat/lon
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cio
import cartopy.feature as cfeature

# lectura del archivo
fname = 'data/rsnc.dat'
data = pd.read_csv(fname, delim_whitespace=True, header=None)
sta = data.iloc[:,0].to_numpy()
lat = data.iloc[:,1].to_numpy()
lon = data.iloc[:,2].to_numpy()

# descargar topografía y fronteras
tiler = cio.Stamen('terrain-background')

proj = ccrs.Mercator()
fig = plt.figure(figsize=(12,10))
ax  = fig.add_subplot(121,projection=proj)
ax.set_extent([-85, -65, -5, 15])
# Adicionar topografía
ax.add_image(tiler, 6)
ax.add_feature(cfeature.BORDERS)
ax.coastlines()
ax.plot(lon,lat,'k^',label='Estaciones',transform=ccrs.Geodetic())
ax.legend()

ax2  = fig.add_subplot(122,projection=proj)
ax2.set_extent([-76, -70, 9, 12])
# Adicionar topografía
ax2.add_image(tiler,10)
ax2.add_feature(cfeature.BORDERS)
ax2.coastlines(resolution='10m')
ax2.plot(lon,lat,'k^',transform=ccrs.Geodetic())

plt.savefig('../figs/chap08_map06.pdf',bbox_inches='tight', pad_inches=0)
plt.show()

