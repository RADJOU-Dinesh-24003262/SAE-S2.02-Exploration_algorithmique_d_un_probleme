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
from Exercice_2.programme3 import calculer_P

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
        debut = time.time()
        valeur_propre_P, vecteur_propre_P = plus_grnd_val_propre(P, taille, i)
        fin = time.time()
        print("temps d'execution : ", fin - debut, "secondes pour une précision de ", i, "entre l'ancien et le nouvel vecteur propre")
        r = vecteur_propre_P

        #Verification
        print("marge d'erreur :", norme((P @ r) - r), "\n")