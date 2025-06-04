# Partie 4 : PageRank - version itérative, analyse
## *Question2 :*

### *Réseau routier : Gaston Berger*

Lors de l'analyse des données de la matrice du réseaux routier de Gaston Berger, nous avons obtenue ses valeurs :
```
Nombre d'itérations : 54
valeur propre : 1.0000001163769396
vecteur propre : [0.01979641 0.02159985 0.01705838 ... 0.01180095 0.01555883 0.0127837 ]
marge d'erreur : 8.273805432419683e-06
Noeud en position :  0   avec comme Identifiant dans la matrice :  267871464
Noeud en position :  1   avec comme Identifiant dans la matrice :  930837874
Noeud en position :  2   avec comme Identifiant dans la matrice :  1853984110
Noeud en position :  3   avec comme Identifiant dans la matrice :  1853984111
Noeud en position :  4   avec comme Identifiant dans la matrice :  1837997530
Noeud en position :  5   avec comme Identifiant dans la matrice :  33782820
Noeud en position :  6   avec comme Identifiant dans la matrice :  302790070
Noeud en position :  7   avec comme Identifiant dans la matrice :  1764753783
Noeud en position :  8   avec comme Identifiant dans la matrice :  1853984104
Noeud en position :  9   avec comme Identifiant dans la matrice :  295252653

Valeur du noeud le plus important
Nom : Pas de nom
Latitude : 43.5192263
Longitude : 5.4466846
Tags : {}
Noeud en position :  1259   avec comme Identifiant dans la matrice :  33651052
Noeud en position :  1258   avec comme Identifiant dans la matrice :  34500867
Noeud en position :  1257   avec comme Identifiant dans la matrice :  255126024
Noeud en position :  1256   avec comme Identifiant dans la matrice :  279036609
Noeud en position :  1255   avec comme Identifiant dans la matrice :  1855845112
Noeud en position :  1254   avec comme Identifiant dans la matrice :  1924158963
Noeud en position :  1253   avec comme Identifiant dans la matrice :  4138831775
Noeud en position :  1252   avec comme Identifiant dans la matrice :  5381442723
Noeud en position :  1251   avec comme Identifiant dans la matrice :  6487992545
Noeud en position :  1250   avec comme Identifiant dans la matrice :  34506214

Valeur du noeud le plus important
Nom : Pas de nom
Latitude : 43.5310691
Longitude : 5.4290631
Tags : {}
```

Comme on peut le voir avec cette copie du terminal, nous extractons de la matrice les 10 noeuds avec les plus grands vecteurs propres, et les 10 avec les plus petit. On analyse aussi les données fournis de noeuds "extrême" par une librairie relié a OpenStreet Map.

Parmis les 10 noeuds les plus "grands", on a 3 Rond-Point et 7 intersections dont 2 d'entres elles sont directements relié a un route importante (routes avec beaucoup de voie, donc beaucoup de circulation), et les autres sont relativements proches de route importante