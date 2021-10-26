# tierra_balon.py
# Dado radio de las diferentes interfases, 
# compare si la Tierra tuviera el tamaño de un 
# balón de Basketball 

import numpy as np

fmt = "%8.1f km %10.5f mm"
R_E = 6371.     # km
R_b = 242.6/2.0 # mm, diametro/2

T_crust  = 25    # km 
T_mantle = 2900
T_ocore  = 2250
T_icore  = 1196
T_atm    = 16

T_batm    = T_atm/R_E*R_b 
T_bcrust  = T_crust/R_E*R_b
T_bmantle = T_mantle/R_E*R_b
T_bocore  = T_ocore/R_E*R_b
T_bicore  = T_icore/R_E*R_b

P_moho   = T_crust
P_cmb    = P_moho+T_mantle
P_icb    = P_cmb+T_ocore

P_bmoho   = T_bcrust
P_bcmb    = P_bmoho+T_bmantle
P_bicb    = P_bcmb+T_bocore

print(" ")
print('     Tierra         Balón  Espesores')
print(fmt %(T_atm, T_batm), ' Atmósfera')
print(fmt %(T_crust, T_bcrust), ' Corteza')
print(fmt %(T_mantle,T_bmantle), ' Manto')
print(fmt %(T_ocore, T_bocore), ' Núcleo Externo')
print(fmt %(T_icore, T_bicore), ' Núcleo Interno')

print('\n')

print('     Tierra         Balón  Prof. Interfase')
print(fmt %(P_moho, P_bmoho), ' Moho')
print(fmt %(P_cmb, P_bcmb), ' CMB')
print(fmt %(P_icb,P_bicb), ' ICB')



