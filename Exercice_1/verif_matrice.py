import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

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

# Convertion de la liste en matrice numpy
Matrice_adjacente = np.array(Web)
print(Matrice_adjacente)


# Création du graphe orienté
G = nx.DiGraph()

# Ajout des arêtes selon la matrice d'adjacence
n = len(Matrice_adjacente)
for i in range(n):
    for j in range(n):
        if Matrice_adjacente[j][i] == 1:
            G.add_edge(j + 1, i + 1)

# Création manuelle des positions pour lisibilité
pos = {
    # Cluster A (fortement lié)
    1: (-3, 3),
    2: (-2, 3),
    3: (-3.5, 2),
    4: (-2.5, 2),
    5: (-2.5, 1),

    # Cluster B (intermédiaire, pont vers A et C)
    6: (-0.5, 1),
    7: (0, 0),
    8: (0.5, 0.5),
    9: (0, -1),

    # Cluster C (fortement lié)
    10: (3, 3),
    11: (2, 2),
    12: (3.5, 2),
    13: (2.5, 1),
    14: (3, 1)
}

print("Liste des noeuds dans G:", list(G.nodes()))
print("Clés dans pos:", list(pos.keys()))


# Affichage
plt.figure(figsize=(12, 8))
nx.draw(
    G, pos, with_labels=True,
    node_size=900, node_color='skyblue',
    font_size=11, font_weight='bold',
    arrows=True, arrowsize=18, arrowstyle='-|>',
    edge_color='dimgray',
)
plt.title("Graphe optimisé du Web", fontsize=15)
plt.axis('off')
plt.tight_layout()
plt.show()