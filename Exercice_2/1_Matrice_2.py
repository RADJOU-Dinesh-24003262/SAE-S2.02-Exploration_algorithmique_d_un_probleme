import numpy as np
# import Exercice_1.programme1 as prog1


import sys
import os
# Ajoute le dossier parent ("SAE 2.02") au chemin Python
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from Exercice_1.Algo_puis_iter_V1 import norme, plus_grnd_val_propre, calculer_Q





if __name__ == "__main__":
        #        1  2  3  4  5
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

        # Calcul du score avec le vecteur propre de Q
        valeur_propre_Q, vecteur_propre_Q = plus_grnd_val_propre(Q, taille)
        r = vecteur_propre_Q

        #Verification
        print("marge d'erreur :", norme((Q @ r) - r))