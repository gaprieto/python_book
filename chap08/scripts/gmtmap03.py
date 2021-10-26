"""
gmtmap03.py
 Mapa Suramérica con limites políticos
"""
import pygmt

reg  = [-85, -35, -60, 15]
proj = 'M0/0/4i'

fig = pygmt.Figure()
fig.coast(
    region=reg,
    projection=proj,
    shorelines=True,
    frame=True,
    resolution='l',
    borders=1,
)
fig.savefig('../figs/chap08_map09.pdf')
fig.show()


