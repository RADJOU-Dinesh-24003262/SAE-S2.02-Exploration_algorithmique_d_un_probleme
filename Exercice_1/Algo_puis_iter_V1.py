import numpy as np

def norme(X) : 
    somme_carr = 0
    for i in X : 
        somme_carr += i**2
    return somme_carr**0.5

def plus_grnd_val_propre(A, taille, e = 10**(-10)) :
    X = np.random.rand(taille)
    X_old = np.zeros(taille)
    compteur = 0
    while norme(X - X_old) > e:
        X_old = X
        temp = A @ X_old
        X = temp/norme(temp)
        compteur += 1
    print("Nombre d'itérations :", compteur)
    print("valeur propre :", norme(A @ X))
    print("vecteur propre :", X)
    return norme(A @ X), X

def calculer_Q(C, taille):
    ## matrice n permettant de savoir le nombre de liens sortants de chaque page
    #matrice_n = np.zeros(taille)
    #for i in range(taille):
    #    for j in range(taille):
    #        if C[i, j] == 1:
    #            matrice_n[j] += 1
    ## matrice Q permettant de savoir le poids de chaque lien
    #Q = np.zeros((taille, taille))
    #for i in range(taille):
    #    for j in range(taille):
    #        if matrice_n[j] != 0:
    #            Q[i,j] = C[i,j] / matrice_n[j]
    #    #Q[:, i] = A[:, i] / norme(A[:, i])
    #return Q
    n = C.shape[0]
    Q = np.zeros_like(C, dtype=float)
    for j in range(n):
        col_sum = C[:, j].sum()
        if col_sum != 0:
            Q[:, j] = C[:, j] / col_sum  # Normalisation
        else:
            Q[:, j] = 1.0 / n  # Cas dangling
    return Q

if __name__ == "__main__":
    Web = [0]*14
    for i in range(14):
        Web[i] = [0]*14

    #              1  2  3  4  5  6  7  8  9 10 11 12 13 14
    Web[1 - 1]  = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    Web[2 - 1]  = [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Web[3 - 1]  = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Web[4 - 1]  = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Web[5 - 1]  = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Web[6 - 1]  = [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
    Web[7 - 1]  = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    Web[8 - 1]  = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    Web[9 - 1]  = [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
    Web[10 - 1] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1]
    Web[11 - 1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1]
    Web[12 - 1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
    Web[13 - 1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
    Web[14 - 1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]

    taille = len(Web)
    
    # Convertion de la liste en matrice numpy
    Matrice_adjacente = np.array(Web)
    print("Matrice adjacente :\n", Matrice_adjacente, "\n")

    # Calcul de la transposée pour C
    C = Matrice_adjacente.transpose()
    print("Matrice C :\n", C, "\n")

    # Calcul de Q
    Q = calculer_Q(C, taille)
    #print("Matrice Q : \n" , Q, "\n")
    print("Q :")
    for row in Q:
        for val in row:
            print(f"{val:5.2}", end="  ")
        print()

    # Calcul du score avec le vecteur propre de Q
    valeur_propre_Q, vecteur_propre_Q = plus_grnd_val_propre(Q, taille)
    r = vecteur_propre_Q

    #Verification
    print("marge d'erreur :", norme((Q @ r) - r), "\nla différence entre Q @ r et r est très petite")
