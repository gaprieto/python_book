# usermult4.py
# Program to multiply 2 numbers, user defined
# until user wants to stop

a = 1
b = 1
while (a!=0 or b!=0):
   intxt = input("Enter two integers (zeros to stop) ")
   a,b = intxt.split()
   a = int(a)
   b = int(b)
   c = a*b
   print ('Product is = ', c)

