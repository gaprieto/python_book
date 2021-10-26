"""
gmtmap06.py
 Con topo, y estaciones lat/lon
"""
import numpy as np
import pandas as pd
import pygmt

# lectura del archivo
fname = 'data/rsnc.dat'
data = pd.read_csv(fname, delim_whitespace=True, header=None)
sta = data.iloc[:,0].to_numpy()
lat = data.iloc[:,1].to_numpy()
lon = data.iloc[:,2].to_numpy()

reg   = [-85, -65, -5, 15]
reg2  = [-76, -70,  9, 12]
proj  = 'M6i'
proj2 = 'M6i'

fig = pygmt.Figure()
pygmt.config(MAP_FRAME_TYPE="plain")
fig.grdimage(
    '@earth_relief_05m',
    region=reg,
    projection=proj,
    cmap='etopo1',
    shading=True,
)
fig.coast(
    region=reg,
    projection=proj,
    shorelines=True,
    water='lightblue',
    borders='1/1p,black',
    frame=True,
#    frame=["WSne", "a"],
)

fig.plot(lon,lat,
    style='t0.15i',
    color='black',
    label='Estaciones',
        )
fig.legend()

fig.shift_origin(xshift='4.5i',yshift='1.5i')
fig.grdimage(
    '@earth_relief_15s',
    region=reg2,
    projection=proj2,
    cmap='etopo1',
    shading=True,
)
fig.coast(
    region=reg2,
    projection=proj2,
    shorelines=True,
    water='lightblue',
    borders='1/1p,black',
    frame='f',
)

fig.plot(lon,lat,
    style='t0.15i',
    color='black',
        )

fig.savefig('../figs/chap08_map12.pdf')
fig.show()

