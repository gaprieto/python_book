import kepler as kep

d_sun   = 150e6 # distancia al sol, en km
T_earth = kep.kepler_3ra(d_sun)
T_days  = T_earth/86400

print('Periodo de órbita terrestre %5.1f días ' %(T_days))

Me        = 5.972e24 # kg
d_sat     = 6371+200 # distancia a la Tierra, en km
T_sat     = kep.kepler_3ra(d_sat,Me)
T_smin    = T_sat/60

print('Periodo de órbita espía %5.1f minutos ' %(T_smin))

