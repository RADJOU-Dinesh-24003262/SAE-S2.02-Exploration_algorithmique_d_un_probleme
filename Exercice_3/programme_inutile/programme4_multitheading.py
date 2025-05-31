import numpy as np

import time

import sys
import os
# Ajoute le dossier parent ("SAE 2.02") au chemin Python
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
parent_dir = os.path.abspath(os.path.join(current_dir, "../.."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from Exercice_1.programme1 import norme, plus_grnd_val_propre, calculer_Q

import threading
def calcul_valeur_propre(epsilon, P, taille):
    debut = time.time()
    valeur_propre_P, vecteur_propre_P = plus_grnd_val_propre(P, taille, epsilon)
    fin = time.time()
    print(f"[Thread] Précision {epsilon} : temps d'exécution = {fin - debut:.6f} s \nMarge d'erreur : {norme((P @ vecteur_propre_P) - vecteur_propre_P)}\n")



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





# Liste des epsilon
epsilons = [1, 1e-5, 1e-10, 1e-20, 1e-100, 1e-200]
threads = []

# Création et démarrage des threads
for eps in epsilons:
    t = threading.Thread(target=calcul_valeur_propre, args=(eps, P, taille))
    threads.append(t)
    t.start()

# Attente de la fin des threads
for t in threads:
    t.join()
