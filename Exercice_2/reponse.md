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

Nous remarquons qu'il y a un problème de type *RuntimeWarning: invalid value encountered in divide* dans la fontion *norme()* de la partie 1. Cela est surement dû à la convergence de la matrice, (ainsi que son vecteur associé) vers 0 (en seulement 4 itérations). Cela est dû au fait le graphe possède deux sources et un pouits, la matrice associé a alors deux colonnes de 0 et une ligne de 0, ce qui fait d'elle une matrice qui ne converge pas avec l'algorithme de puissance itérative.






