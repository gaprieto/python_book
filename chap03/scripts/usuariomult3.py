""" 
usuariomult3.py
Código para multiplicar dos números enteros, 
definidos por el usuario.
Operación se repite hasta que el usuario lo determine.
"""

for i in range(1000):
    intxt = input('Digite dos números enteros (ceros para parar) ')
    a,b   = intxt.split()
    a     = int(a)
    b     = int(b)
    if (a==0 and b==0):
        break
    c = a*b
    print(a,"x",b," = ",c)


