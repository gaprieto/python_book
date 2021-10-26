# gcf.py
# Calculate the greatest common factor (gcf) of two integers

for i in range(10):

   intxt = input("Enter two integers (zeros to stop) ")
   a,b = intxt.split()
   a = int(a)
   b = int(b)

   if (a==0 and b==0):
      break
   else:
      amin = min(a,b)
      for j in range(1,amin+1):
         if ( (a%j)==0 and (b%j)==0):
            jmax = j
   print ("Greatest common factor = ",jmax)

