"""
gcf2.py
encuentre el máximo común divisor de dos números enteros
con una función
"""

def gcf(a,b):
    amin = min(a,b)
    for j in range(1,amin+1):
        if (a%j==0 and b%j==0):
            jmax = j
    return jmax

#------------------------------------
# Ahora, el programa principal
#------------------------------------
for i in range(10):
    intxt = input('Digite dos números enteros (ceros para parar) ')
    a,b   = intxt.split()
    a     = int(a)
    b     = int(b)
    if (a==0 and b==0):
        break
    mcd = gcf(a,b)  # cree esta función

    print ("Máximo común divisor = ", mcd)

