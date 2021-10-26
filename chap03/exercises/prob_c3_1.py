# div2_3.py
# programa imprime una lista de números del 2 al 20, 
# y muestre si el número es divisible por 2, por 3, 
# por ambos o por ninguno. 

print (' ')
print (' Num       Div por 2 y/o 3 ')
print ('----      -----------------')

for i in range(2,20+1):
   if (i%2==0):
      d2 = 1
   else:
      d2 = 0
   if (i%3==0):
      d3 = 1
   else:
      d3 = 0
   
   if (d2==1 and d3 ==1):
      txt = "Ambos"
   elif (d2==1 and d3==0):
      txt = "Por 2"
   elif (d2==0 and d3==1):
      txt = "Por 3"
   else:
      txt = "Ninguno"
   
   print ("%4i %16s"% (i,txt))


