# rand_check.py
# generar 10000 números aleatorios entre 0 y 1. 
# Realice un test de que tan aleatorio es el generador de números, 
# contando el número de veces que el número cae dentro de 10 rangos 
# distintos entre 0 y 1.


import numpy as np

x = np.zeros(10,dtype=int)

for i in range(10000):
   a = np.random.random()
   if (a >=0 and a<0.1):
         x[0]=x[0]+1
   elif (a >=0.1 and a<0.2):
         x[1]=x[1]+1
   elif (a >=0.2 and a<0.3):
         x[2]=x[2]+1
   elif (a >=0.3 and a<0.4):
         x[3]=x[3]+1
   elif (a >=0.4 and a<0.5):
         x[4]=x[4]+1
   elif (a >=0.5 and a<0.6):
         x[5]=x[5]+1
   elif (a >=0.6 and a<0.7):
         x[6]=x[6]+1
   elif (a >=0.7 and a<0.8):
         x[7]=x[7]+1
   elif (a >=0.8 and a<0.9):
         x[8]=x[8]+1
   else:
         x[9]=x[9]+1

print ("0.0 - 0.1 ", x[0])
print ("0.1 - 0.2 ", x[1])
print ("0.2 - 0.3 ", x[2])
print ("0.3 - 0.4 ", x[3])
print ("0.4 - 0.5 ", x[4])
print ("0.5 - 0.6 ", x[5])
print ("0.6 - 0.7 ", x[6])
print ("0.7 - 0.8 ", x[7])
print ("0.8 - 0.9 ", x[8])
print ("0.9 - 1.0 ", x[9])


