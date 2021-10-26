# usermult3.py
# Program to multiply 2 numbers, user defined
# until user wants to stop

for i in range(1000):
   intxt = input("Enter two integers (zeros to stop) ")
   a,b = intxt.split()
   a = int(a)
   b = int(b)
   if (a==0 and b==0):
      break
   c = a*b
   print ('Product is = ', c)

