def rot_mat(Cmat,deg):
    """
    Función para rotar un vector o matriz
    en dos dimensiones en espacio Euclidiano.
    Matriz o vector debe tener shape(2,X), donde
    x puede ser tan grande como quiera
    Entradas: 
      Cmat - matriz o vector a rotar
      deg  - ángulo de rotación, en grados
    Salidas:
      C    - matriz o vector rotado.
    """

    import numpy as np
    
    # convert angle to rad
    alpha = deg/180.0*np.pi
    
    # create rotation matrix
    R = np.zeros((2,2))
    R[0,0] = np.cos(alpha)
    R[0,1] = -np.sin(alpha)
    R[1,0] = np.sin(alpha)
    R[1,1] = np.cos(alpha)
    
    Rt = np.transpose(R)

    C1 = np.matmul(R,Cmat)
    C  = np.matmul(C1,Rt)
    
    return C,R

