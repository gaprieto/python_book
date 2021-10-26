"""
read_stations.py
 Leer archivo con info de estaciones de la RSNC (SGC).
 Columnas separadas por Tabs.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cartopy.crs as ccrs

fname = 'data/rsnc.dat'
data = pd.read_csv(fname, delim_whitespace=True, header=None)
print('Estructura de Pandas')
print(data)

sta = data.iloc[:,0].to_numpy()
lat = data.iloc[:,1].to_numpy()
lon = np.array(data[2])
ele = np.array(data[3])

print('')
print(sta)
print(lat)
print(lon)

# Mapa de los resultados

fig = plt.figure()
ax  = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
ax.set_extent([-90, -60, -5, 15])
ax.stock_img()
ax.coastlines()
ax.plot(lon,lat,'k^')
plt.savefig('../figs/chap06_fig3.pdf',bbox_inches='tight', pad_inches=0)
plt.show()
