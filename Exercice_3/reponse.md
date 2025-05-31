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