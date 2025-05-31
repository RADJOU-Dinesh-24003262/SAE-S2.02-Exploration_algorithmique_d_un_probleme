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