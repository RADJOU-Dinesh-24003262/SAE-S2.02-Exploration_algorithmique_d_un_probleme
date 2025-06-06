import numpy as np
def gauss_elimination(matrix):
    n = len(matrix)

    # Élimination
    for i in range(n):
        # Recherche du pivot
        max_row = i
        for k in range(i+1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Rendre le pivot égal à 1 et éliminer les éléments en dessous
        pivot = matrix[i][i]
        if pivot == 0:
            raise ValueError("Pas de solution unique (pivot nul)")
        for j in range(i, n + 1):
            matrix[i][j] /= pivot

        for k in range(i + 1, n):
            factor = matrix[k][i]
            for j in range(i, n + 1):
                matrix[k][j] -= factor * matrix[i][j]

    # Substitution inverse
    solution = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        solution[i] = matrix[i][n]
        for j in range(i + 1, n):
            solution[i] -= matrix[i][j] * solution[j]
    
    return solution


# Exemple d'utilisation
matrice = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

#resultat = gauss_elimination(matrice)
#print("Solution :", resultat)

#matrice = [[1,-1, 1,-1,  2], [0, 2, 1,-3,  1], [0, 0, 0, 4,  3], [0, 0, 5, 5,-10]]
#print("Solution :", gauss_elimination(matrice))

#M = np.load("Exercice_4/Ex4_data/Gaston_Berger/413 avenue Gaston Berger, Aix en Provence, France_Matrice.npy")
M = [   [0.2,   0.88,   0.46,   0.46,   0.46],  
        [0.2,   0.03,   0.03,   0.46,   0.46],  
        [0.2,   0.03,   0.03,   0.03,   0.03],  
        [0.2,   0.03,   0.46,   0.03,   0.03],  
        [0.2,   0.03,   0.03,   0.03,   0.03]]
  
In = np.identity(len(M))
test = np.array(M) - In

test = test.tolist()

for i in range(len(test)):
    test[i].append(0)

r =  gauss_elimination(test)
print("Solution :", r)