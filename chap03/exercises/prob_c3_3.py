# mcm.py
# Compute the least common multiple of two integers

for i in range(10):
   txtin = input("Digite dos enteros (ceros para parar) ")
   a,b = txtin.split()
   a = int(a)
   b = int(b)
   if (a==0 and b==0):
      break
   else:
      jmin = -a*b
      jmax = -max(a,b)
      for j in range(jmin,jmax+1):
         if (-j%a==0 and -j%b==0):
            jmin = -j
      print ("Mínimo común múltiplo ",jmin)

# Digite dos enteros (ceros para parar) 6 4
# Mínimo común múltiplo  12
# Digite dos enteros (ceros para parar) 2 5
# Mínimo común múltiplo  10
# Digite dos enteros (ceros para parar) 3 15
# Mínimo común múltiplo  15
# Digite dos enteros (ceros para parar) 3 16
# Mínimo común múltiplo  48
# Digite dos enteros (ceros para parar) 0 0

