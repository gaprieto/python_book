# circunf.py
# calcule el volumen y circunferencia
# de una esfera, solicitando el radio
# al usuario. 

import clase.homework as hw

r = 1.0
while (r>0.0):
   r = float(input("Enter the radius (zero to end) "))

   if (r==0):
      break
   elif (r < 0):
      print("No negative values allowed")
      continue
   
   [vol,circf] = hw.v_circf_sph(r)

   print ("Volume and Circumference = %7.2e %7.2e, " % (vol, circf))


# 10
# 4.19e+03 6.28e+01, 
# 2
# 3.35e+01 1.26e+01, 
# 5
# 5.24e+02 3.14e+01, 
# 6371
# 1.08e+12 4.00e+04, 

