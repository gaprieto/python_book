def arr_trab(x):
   """ 
   Función para análisis de unos datos en vector
   Input: x     = array of given size, with numbers
          n     = size of the array
   Output y     = demeaned array
          x_mu  = valor promedio de x
          y_var = variance of array
   """
   import numpy as np

   n     = np.size(x)
   x_mu  = np.mean(x)
   y     = x-x_mu
   y_var = np.var(y)

   return y,x_mu,y_var

