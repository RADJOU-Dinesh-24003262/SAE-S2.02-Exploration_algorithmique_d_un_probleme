# Partie 1 : PageRank - version itérative, premier exemple
## Question 1 :
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
De plus, étant donné que λ = 1, nous pouvons supposer que la matrice est stochastique. 

## Question 3 :
Nous avons ce vecteur de scores, dans l'ordre des pages de 1 à 14:
```
[0.43768811 0.08753762 0.11671683 0.14589604 0.18966485 0.52522573 0.17507524 0.35015049 0.17507524 0.43768811 0.08753762 0.11671683 0.14589604 0.18966485]
```
L'algorithme de la puissance itérée a convergé modérément lentement en 215 itérations en moyenne pour une précision e de 10^-6 ce qui peut paraître élevé pour une matrice 14x14. Nous pouvons remarquer que lamda est assez proche de 1 et la marge d'erreurs est faible.
les pages les plus importantes sont principalement : 
- *la page 1* (score: 0.43768811), car 5 pages pointent vers elle, de plus ces pages sources ont très peu de liens sortants (3 liens au maximum), ce qui augmente le poids du lien vers la page 1.

- *la page 10* (score: 0.43768811), car 5 pages pointent vers elle, malgré que ces pages ont un score faible mais vu qu'elles sont 5 pages avec au maximum 3 liens sortants a pointé vers la pages 10, la quantité de liens entrants fait que le score de la page 10 est élevé.

- *la page 6* (score: 0.52522573), car 3 pages pointent vers elle mais son score élevé est uniquement dû à la page 8 qui lui transmet toute son importance puisqu'elle est la seule page cible de la page 8. Ainsi, un score de 0.35015049 lui est transmis uniquement par la page 8.

- *la page 8* (score: 0.35015049), car malgré que 3 pages pointent vers elle, seul la page 6 lui transmet un tiers de son score (0.52522573/3 = 0.17507524333) et le reste est tranmis à la page 9 et 7. La page 9 et 7, alimentée par la page 6, trasnmetttent leur moitié de leur score à la page 8 (0.17507524/2 = 0.08753762). Ainsi, la page 8 a un score élevé car elle reçoit 2/3 du score de la page 6 que ça soit directement ou indirectement (par la page 9 et 7).   



**les pages 7 et 9 ont un score élevé (grâce à la page 6, une page ayant un gros score qui ne pointent que vers les pages 7, 8, 9). De plus, ces deux pages alimentant la page 8, ont très peu de liens sortants (2 liens), ce qui augmente le poids du lien vers la page 8** 
# **soit a enlever ou a modifier mais pas a garder.**

Nous pouvons remarquer que les pages 6 et 8 se favorisent mutuellement, pour avoir un score élevé.
