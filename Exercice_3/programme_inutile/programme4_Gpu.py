import cupy as np  # np devient GPU

import time

import sys
import os



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
        #print("X_old :", X_old)
        #print("A:", A)
        #print("temp :", temp)
        #print("norme(temp) :", norme(temp))
        #print("\n")
        X = temp/norme(temp)
        compteur += 1
    print("Nombre d'itérations :", compteur)
    print("valeur propre :", norme(A @ X))
    print("vecteur propre :", X, "\n")
    return norme(A @ X), X

def calculer_Q(C, taille):
    # matrice n permettant de savoir le nombre de liens sortants de chaque page
    matrice_n = np.zeros(taille)
    for i in range(taille):
        for j in range(taille):
            if C[i, j] == 1:
                matrice_n[j] += 1
    # matrice Q permettant de savoir le poids de chaque lien
    Q = np.zeros((taille, taille))
    for i in range(taille):
        for j in range(taille):
            if matrice_n[j] != 0:
                Q[i,j] = C[i,j] / matrice_n[j]
        #Q[:, i] = A[:, i] / norme(A[:, i])
    return Q


def calculer_P(C, M, taille, alpha):
    # matrice n permettant de savoir le nombre de liens sortants de chaque page
    matrice_n = np.zeros(taille)
    for i in range(taille):
        for j in range(taille):
            if C[i, j] == 1:
                matrice_n[j] += 1

    P = np.zeros((taille, taille))
    for i in range(taille):
        for j in range(taille):
            if matrice_n[j] != 0:
                P[i, j] = alpha*M[i,j] + (1 - alpha) / taille
            else:
                P[i, j] = 1 / taille
    return P

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
    print("Matrice Q : \n" , Q, "\n")
    
    # Calcul de P
    P = calculer_P(C, Q, taille, 0.85)
    print("Matrice P : \n", P, "\n")

    for i in [1, 1e-5, 1e-10, 1e-20, 1e-100, 1e-200]:
        # Calcul du score avec le vecteur propre de P
        
        np.cuda.Device(0).synchronize()
        debut = time.time()

        valeur_propre_P, vecteur_propre_P = plus_grnd_val_propre(P, taille, i)
        
        np.cuda.Device(0).synchronize()
        fin = time.time()
        print("temps d'execution : ", fin - debut, "secondes pour une précision de ", i, "entre l'ancien et le nouvel vecteur propre")
        r = vecteur_propre_P

        #Verification
        print("marge d'erreur :", norme((P @ r) - r), "\n")