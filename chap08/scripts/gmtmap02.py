"""
gmtmap02.py
 Mapa del globo general con topografía
"""
import pygmt

#proj = 'Moll/-70/4.5i',    
proj = 'G-70/0/4.5i'
fig = pygmt.Figure()
fig.grdimage(
    '@earth_relief_30m',
    region='g',
    projection=proj,
    cmap='globe',
    shading=True,
)

fig.savefig('../figs/chap08_map08.pdf')
fig.show()

proj = 'Moll/-70/4.5i',    
fig = pygmt.Figure()
fig.grdimage(
    '@earth_relief_30m',
    region='g',
    projection=proj,
    cmap='globe',
    shading=True,
)

fig.savefig('../figs/chap08_map08b.pdf')
fig.show()


