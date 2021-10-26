# usermult2.py
# Program to multiply 2 numbers, user defined

intxt = input("Enter two numbers here: ")

a,b = intxt.split()
a = int(a)
b = int(b)
c = a*b

print ('Product is = ', c)
