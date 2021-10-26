"""
gmtmap05.py
 Colombia, rios y fronteras
"""
import pygmt


reg  = [-85, -60, -6, 13]
proj = 'M4i' 
fig = pygmt.Figure()
pygmt.config(MAP_FRAME_TYPE="plain")

fig.coast(
    region=reg,
    projection=proj,
    shorelines=True,
    frame='f',
    resolution='l',
    borders=['1/1p,black','2/1p,gray'],
    water='lightblue',
    land="white",)

fig.shift_origin(xshift='4.2i')  # Shift for next call
fig.coast(
    region=reg,
    projection=proj,
    shorelines=True,
    frame='f',
    resolution='i',
    borders=['1/1p,black'],
    rivers= ['1/blue','2/blue','3/blue'],
    water='lightblue',
    land="white",)
fig.savefig('../figs/chap08_map11.pdf')
fig.show()

