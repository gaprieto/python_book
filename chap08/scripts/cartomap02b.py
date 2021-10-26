"""
cartomap02b.py
 Mapa del globo general com topografía
"""
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

proj = ccrs.Mollweide(central_longitude=-90.0)
fig = plt.figure(figsize=(10,8))
ax  = fig.add_subplot(111,projection=proj)
ax.stock_img()
ax.gridlines(linewidth=1.0)

plt.savefig('../figs/chap08_map02b.pdf',bbox_inches='tight', pad_inches=0)
plt.show()

