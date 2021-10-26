"""
kepler_periodo.py 
    Programa que llama funci´øn propio de Kepler
    para calcular el periodo de órbita de un satélite.
"""

import kepler

d_sun   = 149.59e6 # distancia al sol, en km
T_earth = kepler.kepler_3ra(d_sun)
T_days  = T_earth/86400

print('Periodo de órbita terrestre %5.1f días ' %(T_days))

Me        = 5.972e24 # kg
d_sat     = 6371+200 # distancia a la Tierra, en km
T_sat     = kepler.kepler_3ra(d_sat,Me)
T_smin    = T_sat/60

print('Periodo de órbita espía %5.1f minutos ' %(T_smin))


