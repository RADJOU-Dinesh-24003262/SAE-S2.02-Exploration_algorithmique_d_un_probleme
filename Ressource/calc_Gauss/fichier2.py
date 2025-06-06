import numpy as np

def transvections(S, i_1, i_2, x):
    for c in range(len(S[i_1])):
        S[i_1][c] = S[i_1][c] + (x * S[i_2][c])
    return S


def permutation(S,i_1,i_2):
    S[i_1], S[i_2] = S[i_2], S[i_1]
    return S

def resoudre(Matrice) :
    for i in Matrice :
        print(i)
    print("\n")

    for j in range(len(Matrice[0])) :
        for i in range(len(Matrice)) : 
            for k in range(i, len(Matrice)) :
                if Matrice[i][j] == Matrice[k][j] and Matrice[k][j] != 0  and i != k: #on fait la ligne k - la ligne i s'il sont egale
                    Matrice = transvections(Matrice, k, i, -1)
                    #Matrice = permutation(Matrice, i, k)
                    for ligne in Matrice :
                        print(" ".join(f"{x:5.2f}" for x in ligne))
                    print("\n")

                    


#M = np.load("Exercice_4/Ex4_data/Gaston_Berger/413 avenue Gaston Berger, Aix en Provence, France_Matrice.npy")
M = [   [0.2,   0.88,   0.46,   0.46,   0.46],  
        [0.2,   0.03,   0.03,   0.46,   0.46],  
        [0.2,   0.03,   0.03,   0.03,   0.03],  
        [0.2,   0.03,   0.46,   0.03,   0.03],  
        [0.2,   0.03,   0.02,   0.02,   0.02]]
# M = [[0.5, 0.5, 0],
#      [0.3, 0.3, 1],
#      [0.2, 0.2, 0]]  
In = np.identity(len(M))
a = np.array(M)
test = a - In

determinant = np.linalg.det(test)
print("Déterminant :", determinant)

test = test.tolist()

for i in range(len(test)):
    test[i].append(0)
    print(test[i])
    
somme_colonnes = [sum(colonne) for colonne in zip(*M)]
print("nkkkk",somme_colonnes, "\n")

resoudre(test)