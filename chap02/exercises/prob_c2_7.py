# Dada la velocidad de un movimiento de una placa tectónica
# calcule cuanto se ha desplazado en 1, 8, 60 Ma

import math

fmt2 = 'Edad  %5.0f Ma %5.0f Ma %5.0f Ma'
fmt1 = 'Dist. %5.1f km %5.1f km %5.1f km'
fmtp = 'Prof. %5.1f km %5.1f km %5.1f km'
Pvel = 55.0   # mm/yr

# edad en años
t1 = 1e6      # 1 Ma
t2 = 8e6     # 10 Ma
t3 = 60e6    # 100 Ma

# Distancai en metros
d1 = Pvel*1e-4*t1
d2 = Pvel*1e-4*t2
d3 = Pvel*1e-4*t3

# Prof en metros
ang = 60.
theta = ang*math.pi/180.

p1 = d1*math.sin(theta)
p2 = d2*math.sin(theta)
p3 = d3*math.sin(theta)

print('Con una velocidad de ',Pvel,' mm/yr, la ditance recorrida')
print(fmt2 % (t1/1e6, t2/1e6, t3/1e6))
print(fmt1 % (d1/1000, d2/1000, d3/1000))
print(fmtp % (p1/1000, p2/1000, p3/1000))


