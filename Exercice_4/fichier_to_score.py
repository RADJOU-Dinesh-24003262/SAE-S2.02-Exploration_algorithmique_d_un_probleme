import numpy as np

import time

import sys
import os
# Ajoute le dossier parent ("SAE 2.02") au chemin Python
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from Exercice_1.Algo_puis_iter_V1 import norme, plus_grnd_val_propre, calculer_Q
from Exercice_2.Algo_puis_iter_V2 import calculer_P

fichier1 = "Ressource/Exploration_site/youtube.com/youtube.txt"
fichier2 = "Ressource/Exploration_site/univ-amu.fr/amu.txt"
fichier3 = "Ressource/Exploration_site/riotgames.com/riotgames.txt"

with open(fichier1) as ytb :
    #print(ytb.read())
    matrice_web =[]
    ligne_parasite = 2
    for line in ytb :
        if(ligne_parasite > 0) :
            ligne_parasite = ligne_parasite - 1
            continue

        matrice_ligne = []
        premiere_colone = True
        for i in range(len(line)) :

            if line[i] ==";" and premiere_colone :
                premiere_colone = False

            elif line[i] ==";" and not(premiere_colone):
                matrice_ligne.append(int(line[i + 1]))

        matrice_web.append(matrice_ligne)

    taille = len(matrice_web)

    C = np.array(matrice_web)
    print("Matrice C :\n", C, "\n")

    # Calcul de P directement à partir de C
    P = calculer_P(C, len(C), 0.85)
    #print("Matrice P : \n", P, "\n")
    print("P :")
    for row in P:
        for val in row:
            print(f"{val:7.2}", end="  ")
        print()

    for i in [1e-10]:
        # Calcul du score avec le vecteur propre de P
        debut = time.time()
        valeur_propre_P, vecteur_propre_P = plus_grnd_val_propre(P, taille, i)
        fin = time.time()
        print("temps d'execution : ", fin - debut, "secondes pour une précision de ", i, "entre l'ancien et le nouvel vecteur propre")
        r = vecteur_propre_P

        #Verification
        print("marge d'erreur :", norme((P @ r) - r), "\n")