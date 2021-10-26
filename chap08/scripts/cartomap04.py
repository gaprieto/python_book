"""
cartomap04.py
 Mapa con Tierra y oceano, dos escalas
"""
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature

reg1 = [-170, -100, 20, 60]
reg2 = [-130, -120, 46, 52]
proj = ccrs.Mercator()

fig = plt.figure(figsize=(12,10))
ax1 = fig.add_subplot(2, 1, 1, projection=proj)
ax1.set_extent(reg1)
ax1.add_feature(cfeature.LAND)
ax1.add_feature(cfeature.OCEAN,color='lightblue') 
ax1.coastlines(resolution='50m')
ax1.plot([-130, -130, -120, -120, -130], [46, 52, 52, 46, 46],
         color='red', linestyle='--',
         transform=ccrs.PlateCarree(),
         )

ax2 = fig.add_subplot(2, 1, 2, projection=proj)
box = ax2.get_position()
box.x0 = box.x0 - 0.01
box.x1 = box.x1 - 0.125 
box.y0 = box.y0 + 0.407
box.y1 = box.y1 + 0.407 - 0.125
ax2.set_position(box)
ax2.set_extent(reg2)
ax2.add_feature(
            cfeature.GSHHSFeature(scale='auto'),
            facecolor=cfeature.COLORS['land'],
        )
ax2.patch.set_facecolor('lightblue')

plt.savefig('../figs/chap08_map04.pdf',bbox_inches='tight', pad_inches=0)
plt.show()

