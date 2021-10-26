import numpy as np
import matoper as hw

np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

tau = np.array([[-27.0, -7.1],[-7.1, -13.0]],dtype=float)

print('Tensor de Esfuerzos')
print(tau)

ang = np.arange(-90,90,0.1)

for alpha in ang :
    C2,R = hw.rot_mat(tau,alpha)
    if (abs(C2[0,0])<abs(C2[1,1])):
        continue
    if (abs(C2[1,0])<0.01):
        print('Ángulo rotación %4.1f' %(alpha))
        print('Tensor de Esfuerzos Principales')
        print(C2)
        print('Matriz de rotación')
        print(R)
        print('')

