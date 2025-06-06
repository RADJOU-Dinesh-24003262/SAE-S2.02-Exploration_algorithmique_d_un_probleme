import numpy as np
from scipy.linalg import null_space

Q = np.array([
        [0.2,   0.88,   0.46,   0.46,   0.46],  
        [0.2,   0.03,   0.03,   0.46,   0.46],  
        [0.2,   0.03,   0.03,   0.03,   0.03],  
        [0.2,   0.03,   0.46,   0.03,   0.03],  
        [0.2,   0.03,   0.02,   0.02,   0.02] 
], dtype=float)

I = np.eye(Q.shape[0])
A = I - Q  # (I - Q)


determinant = np.linalg.det(A)
print("Déterminant :", determinant)

# Calcul du noyau de (I - Q)
N = null_space(A)

print("Base du noyau (solutions non nulles de (I - Q)r = 0) :")
print(N)
