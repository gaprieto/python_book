def primos_vector(maxnum):
    """
    prime_vector(maxnum)
    Función que busca números primos entre 2 y maxnum, 
    y los ubica en un arreglo. El programa es muy lento si 
    se buscan primos muy grandes.
    Entradas: 
       maxnum - entero, busqueda de primos hasta maxnum

    Salidas: 
       pvec   - vector con números primos, en orden
       nprime - primos encontrados 
    """
    import numpy as np
    
    prime    = np.zeros(maxnum,dtype=int)
    prime[0] = 1 

    max1 = int(np.floor(np.sqrt(maxnum)))
    for ipos in range(1,max1):
        if (prime[ipos]==0):
            inum   = ipos+1
            max2 = int(np.floor(maxnum/inum)) 
            for j in range(2,max2+1):
                imult = inum*j
                prime[imult-1] = 1
                
    # número de primos, y crear vector
    nprime = np.count_nonzero(prime==0)
    pvec   = np.zeros(nprime,dtype=int)
    pcnt = 0
    for ipos in range(maxnum):
        if (prime[ipos]==0):
            pcnt = pcnt + 1
            inum = ipos + 1
            pvec[pcnt-1] = inum
    
    return pvec,nprime

