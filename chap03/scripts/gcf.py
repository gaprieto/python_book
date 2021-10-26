"""
gcf.py
encuentre el máximo común divisor (gcf)
de dos números enteros
"""

a = None 
b = None
while (a!=0 or b!=0):
    intxt = input('Digite 2 enteros (ceros para parar) ')
    a,b   = intxt.split()
    a     = int(a)
    b     = int(b)
    
    amin = min(a,b)
    if (amin<1):
        break
        
    for j in range(1,amin+1):
        if (a%j==0 and b%j==0):
            jmax = j
    print ("Máximo común divisor = ", jmax)

