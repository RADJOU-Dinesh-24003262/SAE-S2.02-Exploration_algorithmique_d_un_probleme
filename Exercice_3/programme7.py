import numpy as np

import time

import sys
import os
# Ajoute le dossier parent ("SAE 2.02") au chemin Python
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from Exercice_1.programme1 import norme, plus_grnd_val_propre, calculer_Q



def calculer_P(M, taille, alpha):
    # matrice n permettant de savoir le nombre de liens sortants de chaque page
    matrice_n = np.zeros(taille)
    for i in range(taille):
        for j in range(taille):
            if M[i, j] == 1:
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

    Web = [0]*18
    for i in range(18):
        Web[i] = [0]*18

    #              1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18
    Web[1 - 1]  = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Web[2 - 1]  = [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Web[3 - 1]  = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    Web[4 - 1]  = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    Web[5 - 1]  = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    Web[6 - 1]  = [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Web[7 - 1]  = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Web[8 - 1]  = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Web[9 - 1]  = [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    Web[10 - 1] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
    Web[11 - 1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0]
    Web[12 - 1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0]
    Web[13 - 1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0]
    Web[14 - 1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    Web[15 - 1] = [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1]
    Web[16 - 1] = [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Web[17 - 1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Web[18 - 1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
    
    for i in [0, 0.2, 0.5, 0.85, 1]:
        # Calcul de P
        P = calculer_P(Q, taille, i)

        for j in [1e-15]: # à partir de 1e-16, l'algorithme ne converge pas assez (rapidement ou juste ne le permet pas) pour offrir cette précision
            # Calcul du score avec le vecteur propre de P
            debut = time.time()
            valeur_propre_P, vecteur_propre_P = plus_grnd_val_propre(P, taille, j)
            fin = time.time()
            print("temps d'execution : ", fin - debut, "secondes pour une précision de ", j, "entre l'ancien et le nouvel vecteur propre")
            r = vecteur_propre_P

            #Verification
            print("marge d'erreur :", norme((P @ r) - r), "\n")