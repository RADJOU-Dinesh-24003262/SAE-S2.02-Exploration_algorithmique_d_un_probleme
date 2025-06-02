# Partie 3 : PageRank - version itérative, analyse
## *Question 1 :*
Le critère d'arrêt est un facteur primordial pour la précision du résultat fourni, le temps d'execution du programme ainsi que le nombre d'itérations dans la boucle.

Nous avons testé différent e, controlant la presicion du vecteur propre trouvé approximativement, allant de 1 à 1**-200. le e est notre condition d'arrêt, la boucle s'arrete dès que la solution trouvé est assez proche de la vraie solution.
```
Nombre d'itérations : 2
valeur propre : 0.9809599017453005
vecteur propre : [0.55612709 0.13591157 0.15112451 0.21650306 0.25658868 0.46287005 0.10351149 0.24877697 0.10351149 0.34258482 0.12447976 0.14743367 0.16361329 0.24034825]
temps d'execution :  0.02037978172302246 secondes pour une précision de  1 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 0.17831211431474536

Nombre d'itérations : 31
valeur propre : 1.0000000126425392
vecteur propre : [0.46212681 0.11406831 0.14638795 0.17628378 0.22130931 0.44810646 0.16246937 0.30056824 0.16246937 0.46209494 0.11406135 0.14637846 0.17627165 0.22129322]
temps d'execution :  0.0006589889526367188 secondes pour une précision de  1e-05 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 6.177568086746955e-06

Nombre d'itérations : 77
valeur propre : 1.0
vecteur propre : [0.46211057 0.11406475 0.1463831  0.17627757 0.22130106 0.448107 0.1624696  0.30056877 0.1624696  0.46211057 0.11406475 0.1463831 0.17627757 0.22130106]
temps d'execution :  0.0010538101196289062 secondes pour une précision de  1e-10 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 7.496353182151503e-11

Nombre d'itérations : 137
valeur propre : 1.0
vecteur propre : [0.46211057 0.11406475 0.1463831  0.17627757 0.22130106 0.448107 0.1624696  0.30056877 0.1624696  0.46211057 0.11406475 0.1463831 0.17627757 0.22130106]
temps d'execution :  0.0014226436614990234 secondes pour une précision de  1e-20 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 0.0

Nombre d'itérations : 138
valeur propre : 1.0
vecteur propre : [0.46211057 0.11406475 0.1463831  0.17627757 0.22130106 0.448107 0.1624696  0.30056877 0.1624696  0.46211057 0.11406475 0.1463831 0.17627757 0.22130106]
temps d'execution :  0.001413106918334961 secondes pour une précision de  1e-100 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 0.0

Nombre d'itérations : 114
valeur propre : 1.0
vecteur propre : [0.46211057 0.11406475 0.1463831  0.17627757 0.22130106 0.448107 0.1624696  0.30056877 0.1624696  0.46211057 0.11406475 0.1463831 0.17627757 0.22130106]
temps d'execution :  0.0013048648834228516 secondes pour une précision de  1e-200 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 0.0

```
Nous remarquons qu'à partir de 1**-10, l'amélioration de la précision est invisible. Ainsi, nous pouvons en déduire que le critère d'arrêt est suffisant pour une précision de 1**-10.


## *Question 2 :*

Ajout des Pages 15 et 16 qui sont des Hubs et des Pages 17 et 18 qui sont des autorités.  
La page 15 a des liens sortant vers (1, 5, 7, 8, 9, 10, 11, 17, 18)  
La page 16 a des liens sortant vers (1, 2, 6, 7, 8, 9)  
La page 17 a des liens entrant de (11, 12, 13, 14, 15)  
La page 18 a des liens entrant de (3, 4, 5, 15)  

![Graphe pour la partie 3 question 2](https://media.discordapp.net/attachments/1377309792221007963/1378360924322140261/image.png?ex=683c5225&is=683b00a5&hm=59e4406155af3781ef7304d5e6ee2fac92e036d5cde63da3f92b15be8ba3658e&=&format=webp&quality=lossless&width=697&height=400 "Partie 3 question 2")

Pour e = 1e-10 :
```
    Graphe d'origine  |  Nouveau graphe|  Changement  
    1  : 0.46211057   |  0.36026096    |  Diminution  
    2  : 0.11406475   |  0.12278482    |  Augmentation  
    3  : 0.1463831    |  0.14863207    |  Augmentation légère  
    4  : 0.17627757   |  0.15595546    |  Diminution  
    5  : 0.22130106   |  0.19778711    |  Diminution  
    6  : 0.448107     |  0.50108145    |  Augmentation  
    7  : 0.1624696    |  0.20848118    |  Augmentation  
    8  : 0.30056877   |  0.38188994    |  Augmentation  
    9  : 0.1624696    |  0.19953941    |  Augmentation  
    10 : 0.4621105    |  0.31582464    |  Diminution  
    11 : 0.11406475   |  0.11125652    |  Diminution légère  
    12 : 0.1463831    |  0.12993088    |  Diminution  
    13 : 0.17627757   |  0.14310262    |  Diminution  
    14 : 0.22130106   |  0.17047662    |  Diminution  
    15 :              |  0.05259868    |  
    16 :              |  0.05259868    |  
    17 :              |  0.2310204     |  
    18 :              |  0.22792565    |  
```

Les pages 1 et 10 ont connu une forte diminution de leur score cela est dû aux puits qui recueillent leur score des même pages sources que la page 1 et 10, ainsi les pages 1 et 10 partagent leur score avec les pages 18 et 17 qui sont des autorités. Les autorités ont un score moyen voire élevé grâce aux quantité de liens entrant qu'elles possèdent en baisant le score de leur "soeurs" (pages ayant une page source commune).  
Les hubs (les pages 15 et 16) (qu'ils y aient un score élevé ou pas) n'apportent pas spécialement de score aux pages qu'ils pointent, car au vu de leur quantité de lien sortants, leur score est réparti. Ainsi, un l'influence est minime sur les pages "filles" (pages qu'ils repertorient ou pointent). On peut avoir cela à travers la page 2, grâce à l'ajout du hubs 16, la page a gagné environ 0.6 point de score que ça soit directement ou indirectement.


## *Question 3 :*

Méthode : retirer un lien sortant d'une page pour que ses autres liens sortant offrent plus d'importance à la page "fille".

Modification : 
- Page 14, suppression du lien vers page 10
- Page 10, suppression du lien vers page 6

Nous voulons améliorant le score de la page 17, en augmenter le score des pages 11, 12, 13, 14 qui contribuera automatiquement au score de la page 17. De plus, en retirant ces deux liens précis, nous fesons en sorte que tous les liens pointent (directement ou indirectement) vers la page 17. Nous améliorons juste l'absorbance de la page 17. Ainsi, une personne se retrouvant sur la page 10 ou 11 va forcément se retrouver sur la page 17 en continuant de naviguer.
Ainsi, nous nous retrouvons avec ce graphe :

![Graphe pour la partie 3 question 3](https://media.discordapp.net/attachments/1377309792221007963/1378405282983444614/bWNIptcbsokkRUhb.png?ex=683c7b74&is=683b29f4&hm=de7d68af72872fb27853afc32e309e753a1230b159f88817062c6e2d157b9bd3&=&format=webp&quality=lossless&width=790&height=400 "Partie 3 question 3")

Pour e = 1e-10 :
```
     Graphe précédent | Nouveau Graphe |  Changement  
    1  : 0.36026096   | 0.38258594     |  Augmentation   
    2  : 0.12278482   | 0.13372787     |  Augmentation légère  
    3  : 0.14863207   | 0.16163709     |  Aumentation 
    4  : 0.15595546   | 0.1695447      |  Augmentation
    5  : 0.19778711   | 0.21521939     |  Augmentation  
    6  : 0.50108145   | 0.44521595     |  Diminution **forte**  
    7  : 0.20848118   | 0.20037742     |  Diminution légère  
    8  : 0.38188994   | 0.36645657     |  Diminution  
    9  : 0.19953941   | 0.19039707     |  Diminution légère  
    10 : 0.31582464   | 0.25191419     |  Diminution **forte** 
    11 : 0.11125652   | 0.11778432     |  Augmentation légère  
    12 : 0.12993088   | 0.13726885     |  Augmentation légère
    13 : 0.14310262   | 0.15113252     |  Augmentation légère
    14 : 0.17047662   | 0.18008973     |  Augmentation  
    15 : 0.05259868   | 0.05870791     |  Augmentation légère  
    16 : 0.05259868   | 0.05870791     |  Augmentation légère  
    17 : 0.2310204    | 0.3240717      |  Augmentation **forte**  
    18 : 0.22792565   | 0.24955563     |  Augmentation  
```
Nous avons réussi à montrer notre point :  
- La page 17 à augmenté son score de 9 points environ au détriment des pages 6 et 10  qui ont perdu chacune 5 points environ.  

## *Question 4 :*

```
Facteur d'amortissement alpha : 0
Nombre d'itérations : 2
valeur propre : 1.0
vecteur propre : [0.23570226 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226 0.23570226]
temps d'execution :  0.022652864456176758 secondes pour une précision de  1e-10 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 0.0


Facteur d'amortissement alpha : 0.2
Nombre d'itérations : 12
valeur propre : 1.000000000000086
vecteur propre : [0.29458722 0.2125933  0.21904273 0.2194727  0.23796506 0.26591766 0.22282847 0.26662181 0.21510501 0.25853464 0.2103039  0.21652829 0.22044831 0.23122484 0.19308636 0.19308636 0.2832691  0.25040803]
temps d'execution :  0.0004482269287109375 secondes pour une précision de  1e-10 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 8.44202873384422e-12


Facteur d'amortissement alpha : 0.5
Nombre d'itérations : 21
valeur propre : 0.999999999999317
vecteur propre : [0.35469558 0.17802133 0.1947323  0.19751747 0.23485147 0.32995994 0.20474468 0.30387721 0.19178543 0.26913069 0.17043344 0.18453804 0.1939902  0.21686974 0.12959252 0.12959252 0.3296192  0.26087994]
temps d'execution :  0.0007445812225341797 secondes pour une précision de  1e-10 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 3.1555411700047365e-11


Facteur d'amortissement alpha : 0.85
Nombre d'itérations : 45
valeur propre : 1.0000000000072164
vecteur propre : [0.38258594 0.13372787 0.16163709 0.1695447  0.21521939 0.44521595 0.20037742 0.36645657 0.19039707 0.25191419 0.11778432 0.13726885 0.15113252 0.18008973 0.05870791 0.05870791 0.3240717  0.24955563]
temps d'execution :  0.0008296966552734375 secondes pour une précision de  1e-10 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 4.855045942403684e-11


Facteur d'amortissement alpha : 1
Nombre d'itérations : 63
valeur propre : 1.000000000016833
vecteur propre : [0.3654943  0.10620023 0.13608341 0.14604447 0.18782985 0.52732322 0.21194072 0.42112299 0.20642382 0.2326142  0.08880297 0.10793877 0.12171761 0.1485113  0.02758448 0.02758448 0.27791359 0.21860697]
temps d'execution :  0.0009043216705322266 secondes pour une précision de  1e-10 entre l'ancien et le nouvel vecteur propre
marge d'erreur : 6.715581611334766e-11
```


Lorsque le facteur d'amortissement est bas (proche ou égal à 0), plus les vecteurs propre sont généralement plus haut, mais ils sont aussi égaux (lorsque facteur = 0).  
Et dans le cas inverse, lorsque le facteur d'amortissement est haut (proche ou égal à 1), plus les vecteurs sont généralement plus bas en moyenne, mais avec un écart plus grand entre eux.  
Nous pouvons aussi remarquer que plus le facteur d'amortissement est haut, plus le programme prends d'iterations pour converger, ainsi que trouver le vecteur propre associé. Le vecteur propre associé reflète plus la réalité des liens sortants et entrants.

facteur = 0 :
- tout les vecteurs égal a : 0.23570226  
&nbsp;

facteur = 1 :
- vecteurs les plus bas : 0.02758448  
- vecteurs les plus haut : 0.52732322