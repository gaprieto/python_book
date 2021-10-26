def median(data):
   """ 
   Función que calcula la mediana de un arreglo
   Entradas
      data - array with numbers, unsorted
   Salidas
      med - median 
   """
   import clase.homework as hw
    
   d_sorted = hw.quicksort(data)
   n = d_sorted.size

   if (n%2 == 0):   # Even number of data points
      i1 = round(n/2  -1)
      i2 = round(i1+1 )
      med = (d_sorted[i1] + d_sorted[i2])/2.
   else:
      i1 = round((n+1)/2 - 1)
      med = d_sorted[i1]
   
   return med

def mn_std(data):
   """ 
   Función que calcula promedio y 
   desviación estandar.
   Entradas
      data - array with numbers, unsorted
   Salidas
      mn  - promedio (mean)
      std - desviación estandar 
   """
   import numpy as np
    
   n  = data.size
   mn = np.sum(data)/n

   dev = np.sum((data-mn)**2)
   std = np.sqrt(dev/(n))
   
   return [mn, std]


