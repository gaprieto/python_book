"""
anim_mandel.py
"""

"""
anim_mandel.py
"""
def mandel_gif(x0,y0,dx,fname):

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as anim
    import mandel as md

    fig = plt.figure(figsize=(8,10))
    ax = fig.add_subplot(111)
    ax.axis('off')
    ims = []
    for i in range(51):
        dat = md.mandel1(x0,y0,dx)
        im = ax.imshow(dat,cmap='twilight_shifted',animated=True)
        ims.append([im])
        dx = dx/1.5
    
    ani = anim.ArtistAnimation(fig, ims, interval=10, blit=True,
                                repeat_delay=1000)

    writer = anim.PillowWriter(fps=3)  
    ani.save(fname, writer=writer) 
    print('Finished plot ',fname)

#----------------------------------------
# Programa principal
#----------------------------------------

import numpy as np

# Elegir punto de inciio
x0 =-0.21503361460851339
y0 = 0.67999116792639069
dx = 0.8
fname = 'mandel1.gif'
mandel_gif(x0,y0,dx,fname)
 
#-------------------------------------
# Otros puntos interesantes
#-------------------------------------

# Graficar
x0 =-0.77568377
y0 = 0.13646737
dx = 0.8
fname = 'mandel3.gif'


x0 =-0.21503361460851339
y0 = 0.67999116792639069
dx = 0.8
fname = 'mandel1.gif'

x0    = -0.122561
y0    =  0.744862
dx    =  0.8
fname = 'mandel2.gif'



