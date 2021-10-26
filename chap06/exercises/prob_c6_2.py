# prob_c5_2.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

fin  = 'ANDEAN_ARC_part1.csv'
fmt  = '%9.4f %9.4f %9.4f'

data = pd.read_csv(fin,usecols=[4,6,27])
print('DataFrame ')
print(data)

# Option 1
lat  = np.array(data.iloc[:,0])
lon  = np.array(data.iloc[:,1])
SiO2 = np.array(data.iloc[:,2])

print('Opción 1')
for i in range(20):
   print(fmt %(lat[i], lon[i], SiO2[i]))

# Option 2
data_2 = data.to_numpy()
lat_2  = np.array(data_2[:,0])
lon_2  = np.array(data_2[:,1])
SiO2_2 = np.array(data_2[:,2])

print('Opción 2')
for i in range(20):
   print(fmt %(lat_2[i], lon_2[i], SiO2_2[i]))

# Mapa de los resultados

fig = plt.figure(figsize=(20,10))
ax  = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
ax.set_extent([-85, -55, -60, 15])
ax.coastlines()
ax.scatter(lon, lat, c=SiO2)
plt.savefig('chap06_prob2.pdf')

