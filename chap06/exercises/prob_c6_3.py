# prob_c5_3.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fin  = 'ANDEAN_ARC_part1.csv'
fmt  = '%9.4f %9.4f %9.4f'

data = pd.read_csv(fin,usecols=[27,30,34,35,36])
# Option 1
Si  = np.array(data.iloc[:,0])
Al  = np.array(data.iloc[:,1])
Fe  = np.array(data.iloc[:,2])
Ca  = np.array(data.iloc[:,3])
Mg  = np.array(data.iloc[:,4])

# Promedios
Simn = np.nanmean(Si)
Almn = np.nanmean(Al)
Femn = np.nanmean(Fe)
Camn = np.nanmean(Ca)
Mgmn = np.nanmean(Mg)
#Desviaciones
Sistd = np.nanstd(Si)
Alstd = np.nanstd(Al)
Festd = np.nanstd(Fe)
Castd = np.nanstd(Ca)
Mgstd = np.nanstd(Mg)

print('Promedios')
print('    Si,     Al,     Fe,     Ca,     Mg, \n%7.3f %7.3f %7.3f %7.3f %7.3f' 
      %(Simn, Almn,Femn, Camn, Mgmn))
print('Desviación estandar')
print('    Si,     Al,     Fe,     Ca,     Mg, \n%7.3f %7.3f %7.3f %7.3f %7.3f' 
      %(Sistd, Alstd,Festd, Castd, Mgstd))

# Hacer figura por diversión
bins = np.arange(0,30,0.5)

fig = plt.figure(figsize=(20,10))
ax  = fig.add_subplot(1,1,1)
ax.hist(Al,bins=bins,alpha=0.3,label='Al')
ax.hist(Fe,bins=bins,alpha=0.5,label='Fe')
ax.hist(Mg,bins=bins,alpha=0.3,label='Mg')
ax.set_xlim(-1,25)
ax.legend()
ax.set_xlabel('weight %')
plt.savefig('chap06_prob3.pdf')
