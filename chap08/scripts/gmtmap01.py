"""
gmtmap01.py
 Mapa global general
"""
import pygmt

# Proyección Cilíndrica
proj = 'Cyl_stere/180/0/8i'

fig = pygmt.Figure()
fig.coast(
    region='g',
    projection=proj,
    shorelines=True,
    water=False,
    land=False,
    frame=True,
)
fig.savefig('../figs/chap08_map07.pdf')
fig.show()

