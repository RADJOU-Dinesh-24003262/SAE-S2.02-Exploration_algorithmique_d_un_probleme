# Partie 3 : PageRank - version itérative, analyse
*Question 1 :*
Le critère d'arrêt est un facteur primordial pour la précision du résultat fourni, le temps d'execution du programme ainsi que le nombre d'itérations dans la boucle.

Nous avons testé différent e, controlant la presicion du vecteur propre trouvé approximativement, allant de 1 à 10^-15. le e est notre condition d'arrêt, la boucle s'arrete dès que la solution trouvé est assez proche de la vraie solution. De plus, nous avons remarqué que la boucle *while* devient infini dès e >= 1^-16, surement car la suite ne converge pas assez rapidement ou que cette présicion n'est pas permise informatiquement.
```
Nombre d'itérations : 2
valeur propre : 1.0106300334000462
vecteur propre : [0.38771155 0.22341141 0.22341141 0.22341141 0.22341141 0.38771155 0.22341141 0.22341141 0.22341141 0.38771155 0.22341141 0.22341141 0.22341141 0.22341141]
temps d'execution :  0.018985271453857422 secondes pour une précision de 1 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 0.03930298002947658

Nombre d'itérations : 3
valeur propre : 0.9999445290625931
vecteur propre : [0.40122222 0.21680787 0.21680787 0.21680787 0.21680787 0.40122222 0.21680787 0.21680787 0.21680787 0.40122222 0.21680787 0.21680787 0.21680787 0.21680787]
temps d'execution :  0.0004909038543701172 secondes pour une précision de 0.01 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 0.00019598198165530229

Nombre d'itérations : 8
valeur propre : 1.000000474231872
vecteur propre : [0.40115563 0.21684147 0.21684147 0.21684147 0.21684147 0.40115563 0.21684147 0.21684147 0.21684147 0.40115563 0.21684147 0.21684147 0.21684147 0.21684147]
temps d'execution :  0.0003879070281982422 secondes pour une précision de 1e-05 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 1.675860636514159e-06

Nombre d'itérations : 13
valeur propre : 1.0000000000044897
vecteur propre : [0.4011562  0.21684119 0.21684119 0.21684119 0.21684119 0.4011562 0.21684119 0.21684119 0.21684119 0.4011562  0.21684119 0.21684119 0.21684119 0.21684119]
temps d'execution :  0.00041961669921875 secondes pour une précision de 1e-10 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 1.5865752956047422e-11

Nombre d'itérations : 21
valeur propre : 1.0000000000000002
vecteur propre : [0.4011562  0.21684119 0.21684119 0.21684119 0.21684119 0.4011562 0.21684119 0.21684119 0.21684119 0.4011562  0.21684119 0.21684119 0.21684119 0.21684119]
temps d'execution :  0.0004374980926513672 secondes pour une précision de 1e-15 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 2.482534153247273e-16

```

*Question 2 :*

Ajout des Pages 15 et 16 qui sont des Hubs et des Pages 17 et 18 qui sont des autorités.
La page 15 a des liens sortant vers (1, 5, 7, 8, 9, 10, 11, 17, 18)
La page 16 a des liens sortant vers (1, 2, 6, 7, 8, 9)
La page 17 a des liens entrant de (11, 12, 13, 14, 15)
La page 18 a des liens entrant de (3, 4, 5, 15)

Pour e = 1e-15
        Graph d'origin|  Nouveau graph |  Changement
    1  : 0.4011562    |  0.22128172    |  Diminution
    2  : 0.21684119   |  0.22128172    |  Augmentation
    3  : 0.21684119   |  0.22128172    |  Augmentation
    4  : 0.21684119   |  0.22128172    |  Augmentation
    5  : 0.21684119   |  0.22128172    |  Augmentation
    6  : 0.4011562    |  0.40937119    |  Augmentation
    7  : 0.21684119   |  0.22128172    |  Augmentation
    8  : 0.21684119   |  0.22128172    |  Augmentation
    9  : 0.21684119   |  0.22128172    |  Augmentation
    10 : 0.4011562    |  0.22128172    |  Diminution
    11 : 0.21684119   |  0.22128172    |  Augmentation
    12 : 0.21684119   |  0.22128172    |  Augmentation
    13 : 0.21684119   |  0.22128172    |  Augmentation
    14 : 0.21684119   |  0.22128172    |  Augmentation
    15 :              |  0.22128172    |
    16 :              |  0.22128172    |
    17 :              |  0.22128172    |
    18 :              |  0.22128172    |

Les pages aillant déjà un score élevé ont vu leurs score diminué après avoir eu plus de liens entrant (Pages: 1, 10), tandis que les autres pages avec un score de base moins haut ont sûbit une légère augmentation.

*Question 3 :*

Méthode : diminué l'importance d'une page pour que ses liens sortant ai plus d'importance

Modification : Pages 15, suppression du lien vers page 10

Pour e = 1e-15
     Graph précédent  |  Nouveau Graph |  Changement
    1  : 0.22128172   | 0.20922059     |  Diminution
    2  : 0.22128172   | 0.20922059     |  Diminution
    3  : 0.22128172   | 0.20922059     |  Diminution
    4  : 0.22128172   | 0.20922059     |  Diminution
    5  : 0.22128172   | 0.20922059     |  Diminution
    6  : 0.40937119   | 0.38705809     |  Diminution
    7  : 0.22128172   | 0.20922059     |  Diminution
    8  : 0.22128172   | 0.20922059     |  Diminution
    9  : 0.22128172   | 0.20922059     |  Diminution
    10 : 0.22128172   | 0.20922059     |  Diminution
    11 : 0.22128172   | 0.20922059     |  Diminution
    12 : 0.22128172   | 0.20922059     |  Diminution
    13 : 0.22128172   | 0.20922059     |  Diminution
    14 : 0.22128172   | 0.20922059     |  Diminution
    15 : 0.22128172   | 0.20922059     |  Diminution
    16 : 0.22128172   | 0.20922059     |  Diminution
    17 : 0.22128172   | 0.38705809     |  Augmentation
    18 : 0.22128172   | 0.20922059     |  Diminution

Avec un seul lien enlevé, presque toutes les pages ont vu leurs score diminué, sauf la page 17. Vu que la page 15 a moins de liens sortant, sont impact sur la page 17 est donc plus important 

*Question 4 :*

```
facteur d'amortissement = 0
Nombre d'itérations : 2
valeur propre : 1.0
vecteur propre : [0.23570226 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226
 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226
 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226]

temps d'execution :  0.0009992122650146484 secondes pour une précision de  1e-15 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 0.0

facteur d'amortissement = 0.2
Nombre d'itérations : 11
valeur propre : 1.0
vecteur propre : [0.23014365 0.23014365 0.23014365 0.23014365 0.23014365 0.27617239
 0.23014365 0.23014365 0.23014365 0.23014365 0.23014365 0.23014365
 0.23014365 0.23014365 0.23014365 0.23014365 0.27617239 0.23014365]

temps d'execution :  0.001001119613647461 secondes pour une précision de  1e-15 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 0.0

facteur d'amortissement = 0.5
Nombre d'itérations : 14
valeur propre : 1.0
vecteur propre : [0.22086305 0.22086305 0.22086305 0.22086305 0.22086305 0.33129458
 0.22086305 0.22086305 0.22086305 0.22086305 0.22086305 0.22086305
 0.22086305 0.22086305 0.22086305 0.22086305 0.33129458 0.22086305]

temps d'execution :  0.0 secondes pour une précision de  1e-15 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 1.3311106448512297e-16

facteur d'amortissement = 0.85
Nombre d'itérations : 16
valeur propre : 1.0
vecteur propre : [0.20922059 0.20922059 0.20922059 0.20922059 0.20922059 0.38705809
 0.20922059 0.20922059 0.20922059 0.20922059 0.20922059 0.20922059
 0.20922059 0.20922059 0.20922059 0.20922059 0.38705809 0.20922059]

temps d'execution :  0.0009989738464355469 secondes pour une précision de  1e-15 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 0.0

facteur d'amortissement = 1
Nombre d'itérations : 17
valeur propre : 1.0
vecteur propre : [0.20412415 0.20412415 0.20412415 0.20412415 0.20412415 0.40824829
 0.20412415 0.20412415 0.20412415 0.20412415 0.20412415 0.20412415
 0.20412415 0.20412415 0.20412415 0.20412415 0.40824829 0.20412415]
```

temps d'execution :  0.0010004043579101562 secondes pour une précision de  1e-15 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 8.326672684688674e-17


Lorsque le facteur d'amortissement est bas (proche ou égal à 0), plus les vecteurs propre sont généralement plus haut, mais ils sont aussi (lorsque facteur = 0) égaux.
Et dans le cas inverse, lorsque le facteur d'amortissement est haut (proche ou égal à 1), plus les vecteurs sont généralement plus bas, mais avec un écart plus grand entre eux.

facteur = 0
tout les vecteurs égal a : 0.23570226
facteur = 1
vecteurs les plus bas : 0.20412415
vecteurs les plus haut : 0.40824829