def mandel(ax,x1,x2,y1,y2):
    """
    Given the X,Y limits, plot the mandelbrot set
    Requires de axes to plot results
    """
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Define grid size and start matrix
    nx = 200
    ny = 200
    dx = (x2-x1)/float(nx)
    dy = (y2-y1)/float(ny)
    dat = np.zeros((nx,ny))

    # Main loop for each value
    for ix in range(nx):
       for iy in range(ny):
          cr = x1 + dx/2. + dx*float(ix)
          ci = y1 + dy/2. + dy*float(iy)
          # Create complex number
          c = complex(cr,ci)
          z = complex(0.0, 0.0)
          for it in range(1000):
             z = c + z*z
             if (abs(z) > 2):
                break
          dat[ix,iy] = it+1

    # Rotate matrix and plot log10 scale
    dat = np.transpose(dat)
    zdat = np.log10(dat)

    # Plot result 
    ax.imshow(zdat,interpolation='bilinear',
          extent=(x1,x2,y2,y1),cmap='Spectral')

    nsize = 20
    txt = str('{:.1e}').format(nsize*dx)
    tx1 = dx*nx/10+x1
    ty1 = y2-dy*ny/10
    ax.text(tx1,ty1,txt,color='k')
    ax.plot([tx1+5*dx, tx1+nsize*dx+5*dx],[ty1+2*dx, ty1+2*dx],'k')
    ax.axis('equal')
    ax.axis("off")
    ax.set_xticks([])
    ax.set_yticks([])


