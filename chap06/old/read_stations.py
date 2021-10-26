# read_stations.py
# Read seismic station info from the RSNC
# File is Tab delimited

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.basemap import Basemap

fname = 'rsnc3.dat'
data = pd.read_csv(fname, delim_whitespace=True, header=None)

sta = np.array(data[0])
lat = np.array(data[1])
lon = np.array(data[2])
ele = np.array(data[3])
print(sta)
print(lat)

# Plot results
map = Basemap(projection='merc', lat_0 = 4, lon_0 = -72,
    resolution = 'h', area_thresh = 0.1,
    llcrnrlon=-85, llcrnrlat=-2,
    urcrnrlon=-65, urcrnrlat=15)
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'gray')
map.drawmapboundary()
x,y = map(lon, lat)
map.plot(x, y, 'b^', markersize=5)
plt.savefig('chap5_fig3.png') 
plt.show()


