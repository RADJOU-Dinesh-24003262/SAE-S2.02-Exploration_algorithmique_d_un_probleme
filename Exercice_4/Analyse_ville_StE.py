import numpy as np
import sys
import os
from OSMPythonTools.api import Api
import heapq

M = np.load("Exercice_4\\Ex4_data\\Saint_Etienne\\Saint-Etienne, France_Matrice.npy")
Id = np.load("Exercice_4\\Ex4_data\\Saint_Etienne\\Saint-Etienne, France_Id_Noeud.npy")
# Ajoute le dossier parent ("SAE 2.02") au chemin Python
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from Exercice_1.Algo_puis_iter_V1 import norme, plus_grnd_val_propre, calculer_Q
from Exercice_2.Algo_puis_iter_V2 import calculer_P

# Calcul de la transposée pour C
C = M.transpose()

# Calcul de P directement à partir de C
P = calculer_P(C, len(C), 0.85)

# Calcul du score avec le vecteur propre de P
valeur_propre_P, vecteur_propre_P = plus_grnd_val_propre(P, len(C), 1e-5)
r = vecteur_propre_P
#Verification
print("marge d'erreur :", norme((P @ r) - r))

# Trouver les 10 plus grandes valeurs avec leurs indices
plus_grandes = heapq.nlargest(10, enumerate(vecteur_propre_P), key=lambda x: x[1])
print("plus grandes valeur", plus_grandes)
for i in range(len(plus_grandes)):
    print(Id[plus_grandes[i][0]])

api = Api()
node = api.query('node/' + str(Id[(vecteur_propre_P.tolist()).index(max(vecteur_propre_P))]))

# Affichage des données principales
print("Nom :", node.tags().get("name", "Pas de nom"))
print("Latitude :", node.lat())
print("Longitude :", node.lon())
print("Tags :", node.tags())

# Somme des colonnes
somme_colonnes = P.sum(axis=0)
print("Sommes des colonnes :", somme_colonnes)

# Vérification stochastique (colonne)
est_stochastique = np.allclose(somme_colonnes, 1.0)
print("La matrice est stochastique par colonne :", est_stochastique)
