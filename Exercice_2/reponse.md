# Partie 2 : PageRank - version itérative, deuxième exemple
# ## Question 1 :
En applicant l'algorithme de la 1° partie sur le graphe de la partie 2, nous avons comme résultat: 
```
Matrice adjacente :     
 [[0 0 0 0 0]           
 [1 0 0 0 0]            
 [1 0 0 1 0]            
 [1 1 0 0 0]            
 [1 1 0 0 0]]           
 
Matrice C :
 [[0 1 1 1 1]
 [0 0 0 1 1]
 [0 0 0 0 0]
 [0 0 1 0 0]
 [0 0 0 0 0]]

Matrice Q :
 [[0.  1.  0.5 0.5 0.5]
 [0.  0.  0.  0.5 0.5]
 [0.  0.  0.  0.  0. ]
 [0.  0.  0.5 0.  0. ]
 [0.  0.  0.  0.  0. ]]

d:\but 1 info\S2\SAE 2.02\Exercice_1\programme1.py:16: RuntimeWarning: invalid value encountered in divide
  X = temp/norme(temp)
Nombre d'itérations : 4
valeur propre : nan
vecteur propre : [nan nan nan nan nan]

marge d'erreur : nan    
```

Nous remarquons qu'il y a un problème de type *RuntimeWarning: invalid value encountered in divide* dans la fontion *norme()* de la partie 1. Cela est surement dû à la convergence de la matrice, (ainsi que son vecteur associé) vers 0 (en seulement 4 itérations). Cela est dû au fait le graphe possède deux sources et un puit, la matrice associé a alors deux colonnes de 0 et une ligne de 0, ce qui fait d'elle une matrice qui ne converge pas avec l'algorithme de puissance itérative.

# ## Question 2 :
En applicant la matrice de transition, les scores obtenues sont:

- Page 1 : 0.67904198
- Page 2 : 0.36704972
- Page 3 : 0.36704972
- Page 4 : 0.36704972
- Page 5 : 0.36704972

Les pages de 2 à 5 ont un score égal, leur points commun sont quelles ont toutes des liens sortants, tandis que la pages 1 avec un score plus élevé est un puit.
