#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# kepler_3ra.py
# 
def kepler_3ra(a,M=1.98847e30):
    """ 
    Función que usa la ecuación de la 3ra ley de 
    Kepler, para calcular el periodo para completar
    una órbita. 
    Entradas:
       a - distancia en km del satélite con respecto 
           al centro del cuerpo (planeta, sol, etc)
       M - Masa del cuerpo (default - Masa del sol)
    Salidas:
       T - Periodo para completar una órbita, en 
           segundos
    """
    
    import numpy as np
    
    G = 6.67430e-11 # m3⋅kg−1⋅s−2
  
    a_m = a * 1000.0   # in m
    
    T = np.sqrt(4.0 * np.pi**2 * a_m**3/(G*M))
    
    return T

      

