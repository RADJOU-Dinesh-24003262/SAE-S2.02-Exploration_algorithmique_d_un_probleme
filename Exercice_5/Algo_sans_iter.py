#On rappelle que le vecteur de score est solution du systeme ` r = Pr. En deduire un  ´
#algorithme de calcul direct (c’est-a-dire de calcul exact et sans approximations successives) `
#du score r. Ecrire le pseudo-code correspondant a cet algorithme.

import numpy as np

#det(Q −λIN) = 0

#mais étant donné que la matrice P est stochastique la somme des colonnes est égale à 1, ainsi que lambda
#donc nous aons : det(P - I) = 0
P = [0]*14
for i in range(14):
   P[i] = [0]*14
P = np.array(P)

I = np.identity(len(P))

#Ainsi, nous devons calculer directement le vecteur propre avec AX = λX => AX = X
#Nous devons utiliser le pivot de Gauss pour résoudre cette équation
