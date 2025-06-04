import numpy as np

import sys
import os
# Ajoute le dossier parent ("SAE 2.02") au chemin Python
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from Exercice_1.Algo_puis_iter_V1 import norme, plus_grnd_val_propre, calculer_Q

def calculer_P(C, M, taille, alpha):
    ## matrice n permettant de savoir le nombre de liens sortants de chaque page
    #matrice_n = np.zeros(taille)
    #for i in range(taille):
    #    for j in range(taille):
    #        if C[i, j] == 1:
    #            matrice_n[j] += 1
    #P = np.zeros((taille, taille))
    #for i in range(taille):
    #    for j in range(taille):
    #        if matrice_n[j] != 0:
    #            P[i, j] = alpha*M[i,j] + (1 - alpha) / taille
    #        else:
    #            P[i, j] = 1 / taille
    #return P
    n = C.shape[0]
    P = alpha * Q + (1 - alpha) / n * np.ones((n, n))
    return P

if __name__ == "__main__":

#                1  2  3  4  5
        Web =  [[0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 1, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0]]

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
        
        # Calcul de P
        P = calculer_P(C, Q, taille, 0.85)
        #print("Matrice P : \n", P, "\n")
        print("P :")
        for row in P:
            for val in row:
                print(f"{val:5.2}", end="  ")
            print()

        # Calcul du score avec le vecteur propre de P
        valeur_propre_P, vecteur_propre_P = plus_grnd_val_propre(P, taille, 1e-10)
        r = vecteur_propre_P

        #Verification
        print("marge d'erreur :", norme((P @ r) - r))