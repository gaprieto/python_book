# Gravity in space
#

import numpy as np
import clase.homework as hw

g0 = hw.grav_acel(0.0)
print('Gravedad en superficie %7.4f' % (g0))

for i in range(6):
    alt1 = 10**(i)
    dgrav = hw.comp_grav(alt1)
    print('Proporción a %7.0f km de altura = %7.4f' % (alt1,dgrav))

