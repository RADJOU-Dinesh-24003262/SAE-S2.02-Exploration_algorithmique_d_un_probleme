#On rappelle que le vecteur de score est solution du systeme ` r = Pr. En deduire un  ´
#algorithme de calcul direct (c’est-a-dire de calcul exact et sans approximations successives) `
#du score r. Ecrire le pseudo-code correspondant a cet algorithme.

import numpy as np

#det(Q −λIN) = 0


Q = [0]*14
for i in range(14):
    Q[i] = [0]*14
    
I = np.identity(len(Q))
print(I)
print(I*2)
