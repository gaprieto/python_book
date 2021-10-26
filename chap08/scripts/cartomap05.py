"""
cartomap05.py
 Colombia, rios y fronteras
"""
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

proj4 = ccrs.Mercator()

fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(1, 2, 1, projection=proj4)
ax.set_extent([-85, -60, -6, 13])

# Descargue info de fronteras y ríos de Natural Earth Data
countries = cfeature.NaturalEarthFeature(
    category='cultural',
    name = 'admin_0_boundary_lines_land',
    scale='10m',
    facecolor='none',
)
states = cfeature.NaturalEarthFeature(
    category='cultural',
    name = 'admin_1_states_provinces',
    scale='10m',
    facecolor='none',
)

rivers = cfeature.NaturalEarthFeature(
    'physical',
    'rivers_lake_centerlines',
    '10m',
)


# Add paises y rios
ax.add_feature(cfeature.OCEAN,color='lightblue')
ax.add_feature(states,edgecolor='lightgrey',linestyles='-')
ax.add_feature(countries,edgecolor='k')
#ax.add_feature(rivers,edgecolor='lightblue',facecolor='none')

# Lineas de costa
ax.coastlines(resolution='10m')

ax2 = fig.add_subplot(1, 2, 2, projection=proj4)
ax2.set_extent([-85, -60, -6, 13])

# Add paises y rios
ax2.add_feature(cfeature.OCEAN,color='lightblue')
#ax.add_feature(states,edgecolor='lightgrey',linestyles='-')
ax2.add_feature(rivers,edgecolor='blue',facecolor='none')
ax2.add_feature(countries,edgecolor='k')

# Lineas de costa
ax2.coastlines(resolution='10m')

plt.savefig('../figs/chap08_map05.pdf',bbox_inches='tight', pad_inches=0)
plt.show()

