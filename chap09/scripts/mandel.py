def mandel1(x0=-0.21503361460851339,
            y0=0.67999116792639069,
            dx=0.2):
    
    import numpy as np

    # defina la grilla
    nx  = 300
    x   = np.linspace(x0-dx,x0+dx,nx)
    y   = np.linspace(y0-dx,y0+dx,nx)
    dat = np.zeros((nx,nx))

    # Calcular Z con un loop
     # triple loop = x, y, y para calcular 1000 veces z.

    for ix in range(nx):
        for iy in range(nx):
            cr = x[ix]
            ci = y[iy]
            # create complex c
            c = complex(cr,ci)
            z = complex(0.0,0.0)
            for it in range(1000):
                z = c + z*z
                if (abs(z)>2.0):
                    break       
            dat[ix,iy] = it+1
    dat = np.transpose(dat)
    dat = np.log10(dat)

    return dat

