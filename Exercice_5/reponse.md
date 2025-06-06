# Partie 5 : PageRank - calcul direct des scores et comparaisons d’algorithmes
## *Question 1*
Étant donné que la matrice P est une matrice Stochastique, sa valeur propre est 1. 
Donc nous passons de QX = λX à QX = X 
Soit, n la taille de la matrice Q : 
*X = QX* ≡ *X - QX = 0* ≡ *(In - Q)X = 0*
  
(In - Q)X est peut être représenter par un système linéaire à n équations et n inconnus donc il n'existe pas une infinité de solutions mais un vecteur propre unique   
  
Ainsi, nous nous retrouvons avec un système à n équations et n inconnus qui peut être résolus avec le pivot de Gauss ou sinon avec un algorithme de résolution d'algorithme (méthode de point fixe ou Algorithme de dichotomie) mais ses algorithmes donnent une approximation et non, la valeur exacte.    

```
#soit Q la matrice sur laquelle il faut calculer le vecteur propre et la valeur propre
n = taille(Q)
In = Matrice_identité(n) 
Matrice_test = (In - Q)
Matrice_test = Matrice_test + ajout_colone(0)
#Maintenant avec cette matrice, on peut appliquer le programme du théorème du Gauss qu'on a crée au premier semestre R1.07.


```





X = QX 
X(QX)⁻1 = In
X Q^-1 X⁻1 = 1
