import cartopy
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader

# Create a feature for States/Admin 1 regions 
# at 1:50m from Natural Earth
    
states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_2_states_provinces_lines',
        scale='50m',
        facecolor='none')


ax = plt.axes(projection=cartopy.crs.PlateCarree())

ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.COASTLINE)
ax.add_feature(cartopy.feature.BORDERS, linestyle=':')
ax.add_feature(cartopy.feature.STATES, edgecolor='gray')
ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
ax.add_feature(cartopy.feature.RIVERS)
#ax.add_feature(states_provinces, edgecolor='gray')

# lon1, lon2, lat1, lat2
ax.set_extent([-90, -60, -10, 20])


#
# Read shapefile del DANE
#

reader = shpreader.Reader('91_AMAZONAS/ADMINISTRATIVO/MGN_DPTO_POLITICO.shp')

print(reader.records())

plt.show()


