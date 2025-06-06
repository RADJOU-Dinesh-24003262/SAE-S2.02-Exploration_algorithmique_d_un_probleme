# Partie 2 : PageRank - version itérative, deuxième exemple
## Question 1 :
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

Nous remarquons qu'il y a un problème de type *RuntimeWarning: invalid value encountered in divide* dans la fontion *norme()* de la partie 1. Cela est surement dû à la convergence de la matrice, (ainsi que son vecteur associé) vers 0 (en seulement 4 itérations). Cela est dû au fait le graphe possède deux sources et un puit, la matrice associé a alors deux colonnes de 0 et une ligne de 0, ce qui fait d'elle une matrice qui ne converge pas avec l'algorithme de puissance itérative. Le fait qu'un sommet soit un puit est un problème majeur. Un sommet ne possédant aucun lien sortant, en anologie dans le monde réel, représente qu'un personne se retrouvera piégé dans une page sans revenir en arrière. Les colonnes nuls et lignes posent problèmes car en multipliant la matrice **Q** par le vecteur propre **r**, ce qui pose problème.

## Question 2 :
α, representant la probabilité que les utilisateurs suivent les liens du graphes dans le monde réel, est le facteur d'amortissement permettant d'avoir des colonnes et lignes non nuls en répartissant (1 - α)% soit 15% du score de chaque page vient de toute les pages, ce qui permet de mettre en place que l'utilisateur peux venir de nul part. Si une page n'a pas de lien sortant alors tout son score sera réparti équitabelement à toutes les pages puisque l'ulisateur se retouvant dans un *"puit"* alors ira dans une page au hasard du web.  

En applicant l'algorithme sur la matrice de transition P, les scores obtenues sont:

- Page 1 : 0.82582244
- Page 2 : 0.40102189
- Page 3 : 0.19748693
- Page 4 : 0.28141887
- Page 5 : 0.19748693

La page 1 a le score le plus élevé car elle possède un lien entrant de toutes les autres pages. Les pages 3 et 5 ont le score le plus faible car ils n'ont aucun lien entrant. La page 2 et 4 ont un score moyen parce qu'elles ont un lien entrant qui font légèrement augmenté leur score. Ainsi, on peut en déduire que le résultat fourni est cohérent par rapport au graphe.

# ///// Manque la justification que le vecteur de score est approximativement r = Pr //////
