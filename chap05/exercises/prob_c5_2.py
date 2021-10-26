# Promedio y medianas
#

import numpy as np
import clase.homework as hw
import stats_hw as st

n = 51
# Normal distribution, mean=0, std=1
C = np.random.normal(0,1,51)

med = st.median(C)
[mean,std] = st.mn_std(C)

print("Número de puntos ", n)
print("Prom y std       %6.3f %6.3f %6.3f %6.3f" % (mean, std, np.mean(C), np.std(C)))
print("Mediana          %6.3f %6.3f" % (med, np.median(C)))
print('Arreglo organizado')
print(hw.quicksort(C))

print('')
n = 50
# Normal distribution, mean=0, std=1
D = np.random.normal(0,1,50)

med = st.median(D)
[mean,std] = st.mn_std(D)

print("Número de puntos ", n)
print("Prom y std       %6.3f %6.3f %6.3f %6.3f" % (mean, std, np.mean(D), np.std(D)))
print("Mediana          %6.3f %6.3f" % (med, np.median(D)))
print('Arreglo organizado')
print(hw.quicksort(D))


