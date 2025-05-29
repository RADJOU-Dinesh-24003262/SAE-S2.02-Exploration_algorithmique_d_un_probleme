*Question 1 :*
L'algorithme de la puissance itérée permet de calculer : 
    - La plus grande valeur  propre d'une matrice,
    - Son vecteur propre associé.
D'après le cours (section 3.4), nous avons :
    AX = λX
où A est la matrice, X est le vecteur propre et λ est la valeur propre.

Nous cherchons, dans cette situation, à calculer le score de chaque page web, soit calculer : 
    r = Qr 
où r est le vecteur des scores et Q la matrice permettant de calculer les scores des pages web en fonction du nombre de liens présents dans la page source. 
**Ainsi, nous avons également : 
    Q = [q_ij] 
où q_ij représente le poids du lien de la page j vers la page i.**

Ainsi nous pouvons remarquer : 
    AX = λX ↔ Qr = r 
où Q = A, r = X et λ = 1 (r est un vecteur propre de Q).
La résolution de cette équation est un cas particulier de l'algorithme de la puissance itérée où nous cherchons à calculer le vecteur propre associé à la valeur propre λ = 1.
Ainsi, nous pouvons appliquer l'algorithme de la puissance itérée pour calculer le score des pages web.

*Question 3 :*
#Analyser la pertinence du resultat obtenu
L'algorithme de la puissance itérée a convergé rapidement en 215 itérations en moyenne pour une précision e de 10^-6 ce qui peut paraître élevé. Nous pouvons remarquer que lamda est assez proche de 1 et la marge d'erreurs est faible.
les pages les plus importantes sont principalement : 
    - la page 1 (score: 0.43768811), car 5 pages pointent vers elle, de plus ces pages sources ont très peu de liens sortants (3 liens au maximum), ce qui augmente le poids du lien vers la page 1.

    - la page 8 (score: 0.35015049), car 

    - la page 6 (score: 0.52522573), car 3 pages pointent vers elles mais son score est si élevé est uniquement grâce à la page 8 qui lui transmet toute son importance puisqu'elle est la seule page cible de la page 8. Ainsi, un score de 0.35015049 lui est transmis uniquement par la page 8.
    
    - la page 10 (score: 0.43768811),
