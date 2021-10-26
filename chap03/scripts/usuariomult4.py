# usuariomult4.py
# Código para multiplicar dos números enteros, 
# definidos por el usuario.
# Operación se repite con while loop.
#

a = None 
b = None

while (a!=0 or b!=0):
    intxt = input('Digite dos números enteros (ceros para parar) ')
    a,b   = intxt.split()
    a     = int(a)
    b     = int(b)
    c     = a*b
    print(a,"x",b," = ",c)

