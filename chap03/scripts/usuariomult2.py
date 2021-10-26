# usuariomult2.py
# Código para multiplicar dos números enteros, 
# definidos por el usuario.
# Una sola solicitud para los dos números.
#

intxt = input("Digite dos números enteros: ")
a,b = intxt.split()
a = int(a)
b = int(b)

c = a*b

print(a,"x",b," = ",c)

