"""
gmtmap04.py
 Mapa con Tierra y oceano, dos escalas
"""
import pygmt

reg1 = [-170, -100, 20, 60]
reg2 = [-130, -120, 46, 52]

fig = pygmt.Figure()
fig.coast(
    region=reg1,
    projection='M8i',
    shorelines=True,
    water='lightblue',
    land='grey',
    frame=True
)
fig.plot([-130, -120, -120, -130, -130],[46, 46, 52, 52, 46],
        pen="2p,red,-"
        )

pygmt.config(MAP_FRAME_TYPE="plain")
fig.shift_origin(xshift='0.2i',yshift='0.1i')  # Shift for next call
fig.coast(
    region=reg2,
    projection='M4i',
    shorelines=True,
    water='lightblue',
    land='grey',
    frame='f'
)

fig.savefig('../figs/chap08_map10.pdf')
fig.show()

