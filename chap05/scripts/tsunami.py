"""
tsunami.py
Velocidad de onda de tsunami
"""
import numpy as np

g     = 9.8  # m/s
depth = 5000 # m
T     = 1800 # s, 30 min
h     = 1    # m wave height
rho   = 1    # kg/m3

V = np.sqrt(g*depth)
L = V*T

F = 1/8 * g * V * rho * h**2

print('Para un tsunami')
print('   Prof. del océano  = %4.1f m' %depth)
print('   Periodo           = %4.1f min' %(T/60))
print('   Altura Ola (h)    = %4.1f m' %(h))
print('')

print('Velocidad (V)    = %4.1f km/h'%(V/1000*3600))
print('Long de Onda (L) = %4.1f km' %(L/1000))

# Asuma que no hay perdida de energía (E_k es constante)
# y el periodo de la onda no cambia
# calcule la velocidad, longitud de onda y altura 
# de la ola para una playa 
# de 25 m de profundidad.

depth = np.array((2000,1000,500,100,50,25,10))
V     = np.sqrt(g*depth)
L     = V*T
h     = np.sqrt(8*F/(V * rho * g))


ndep = len(depth)
print('')
print('Prof(m)  V(km/s)  L(km)   h(m)')
for i in range(ndep):
    print('   %4i    %5.1f  %5.1f  %5.1f' 
          %(depth[i],V[i]/1000*3600,L[i]/1000,h[i]))
    

