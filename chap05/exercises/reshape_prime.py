def reshape_prime(primes,isize=4):
    """
    Función para crear matriz en esperial
    con un número máximo de tamaño (nxn)
    El vector primes, debe tener los números
    primos que se quieren organizar
    Entradas:
       primes - arreglo con números en orden
    Opcional
       isize - tamaño de la matriz cuadrada
    Salidas
       c - matrix cuadrada en espiral
    """
    import numpy as np

    c = np.zeros((isize,isize))

    if (isize%2 == 1):
        i0 = round((isize+1)/2-1)
    else:
        i0 = round(isize/2)-1

    # Initial point
    i1 = i0
    j1 = i0
    c[i1,j1]=primes[0]

    # loop over spiral
    icnt = 0
    for k in range(isize):
        k0 = k+1
        if (k0%2 == 1):
            iplus = +1
        else:
            iplus = -1
        for j in range(k0):
            j1 = j1+1*iplus
            if (i1==isize or j1==isize or
                  i1< 0     or j1< 0):
                break
            icnt = icnt+1
            c[i1,j1] = primes[icnt]
        for i in range(k0):
            i1 = i1+1*iplus
            if (i1==isize or j1==isize or
                    i1< 0     or j1< 0):
                break
            icnt = icnt+1
            c[i1,j1] = primes[icnt]

    return c

