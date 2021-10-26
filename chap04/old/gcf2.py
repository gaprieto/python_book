# gcf2.py
# Calculate the greatest common factor (gcf) of two integers
# using a User defined function


# Define user function
def getgcf(x,y):
   amin = min(x,y)
   for j in range(1,amin+1):
      if ( (x%j)==0 and (y%j)==0):
         jmax = j
   z = jmax  
   x = 143
   y = 345
   return z

# Start the main code

for i in range(10):

   intxt = input("Enter two integers (zeros to stop) ")
   a,b = intxt.split()
   a = int(a)
   b = int(b)

   if (a==0 and b==0):
      break
   else:
      gcf = getgcf(a,b)
   print ("Greatest common factor = ",gcf)
   print (a,b)

