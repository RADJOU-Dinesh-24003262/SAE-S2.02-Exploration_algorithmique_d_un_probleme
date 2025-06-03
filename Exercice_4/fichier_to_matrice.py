

with open("../Ressource/Exploration_site/youtube.com/youtube.txt") as ytb :
    #print(ytb.read())
    matrice_ytb =[]
    ligne_parasite = 2
    for line in ytb :
        if(ligne_parasite > 0) :
            ligne_parasite = ligne_parasite - 1
            continue

        matrice_ligne = []
        premiere_colone = True
        for i in range(len(line)) :

            if line[i] ==";" and premiere_colone :
                premiere_colone = False

            elif line[i] ==";" and not(premiere_colone):
                matrice_ligne.append(int(line[i + 1]))

        matrice_ytb.append(matrice_ligne)

    for line in matrice_ytb :
        print(line)