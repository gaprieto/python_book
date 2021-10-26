# quad_raiz.py
# Usando la formula cuadrática para despejar x
# Entradas: a, b, c
# Salidas:  x1 y x2, los dos posibles valores
# La formula es a*x**2+b*x+c = 0
#

for i in range(10):
   intxt = (input("Digite 3 números para ax**2+bx+c=0 (ceros para parar) "))
   a,b,c = intxt.split()
   a = float(a)
   b = float(b)
   c = float(c)
   # Check exit loop
   if (a == 0 and b == 0 and c == 0):
      break
   # Check if all zeroes
   if (a ==0 and b == 0):
      print("No hay valores de x, c debe ser cero")
      continue
   elif (4*a*c > b**2):
      print("No hay valores reales")
      continue
   elif (a == 0): 
         x1 = -c/b          # si a = 0, despejar
         print("Sólo hay un valores posible x = ", x1)
         continue
   else:   
         x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
         x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)     
         print("Hay 2 valores reales para x: ", x1, " and ", x2)


# Algunos resultados
# Digite 3 números para ax**2+bx+c=0 (ceros para parar) 2 4 2
# Hay 2 valores reales para x:  -1.0  and  -1.0
# Digite 3 números para ax**2+bx+c=0 (ceros para parar) 2 8 4
# Hay 2 valores reales para x:  -0.5857864376269049  and  -3.414213562373095
# Digite 3 números para ax**2+bx+c=0 (ceros para parar) 0 2 4
# Sólo hay un valores posible x =  -2.0
# Digite 3 números para ax**2+bx+c=0 (ceros para parar) 4 2 5
# No hay valores reales
# Digite 3 números para ax**2+bx+c=0 (ceros para parar) 0 0 0


