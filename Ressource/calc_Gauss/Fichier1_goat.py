import numpy as np


def permutation(S,i_1,i_2):
    S[i_1], S[i_2] = S[i_2], S[i_1]
    return S

def dilatation(S,i,x):
    for c in range(len(S[i])):
        S[i][c] = S[i][c] * x
    return S

def transvections(S, i_1, i_2, x):
    for c in range(len(S[i_1])):
        S[i_1][c] = S[i_1][c] + (x * S[i_2][c])
    return S

def est_membre_gauche_nul(E):
    for i in E[0:len(E)-1]:
        if (i > 1e-10):
            return False
    return True

def ligne_a_simplifier(S):
    for i in range(len(S)):
        if (est_membre_gauche_nul(S[i])) :
            return i 
    return -1

def simplifier(S):
    liste_indices = []
    for i in range(len(S)):
        if est_membre_gauche_nul(S[i]):
            if S[i][len(S[i]) - 1] < 1e-10:
                liste_indices.append(i)
            else:
                return False, []
            
    for i in liste_indices[-1::-1]:
        del S[i]
    return True, S

def coordonnees_pivot(S,k):
    coord = [len(S),len(S)]
    for i in range(k,len(S)):
        for j in range(0,len(S[i]) -1):
            if S[i][j] != 0 and  coord[1] > j:
                coord = [i,j]
               
    return coord

def pivoter(S,k):
    coord_pivot = coordonnees_pivot(S,k)
    #print(S, coord_pivot, "\n")

    #if coord_pivot[0] == len(S) :
        #return S
        #sys.exit("Erreur : pas de pivot trouvé à partir de la ligne " + str(k))

    if coord_pivot[0] != k:
        S = permutation(S,coord_pivot[0], k)
    coord_pivot[0] = k
    if k > len(S) : 
        return S
    pivot_val = S[coord_pivot[0]][coord_pivot[1]]
    #if pivot_val != 1:
    #     S = dilatation(S, k, 1/pivot_val)
    i = k+1
    while i < len(S):
        if S[i][coord_pivot[1]] != 0:
            x = - S[i][coord_pivot[1]]/pivot_val
            # print("transvection :" ,S[i][coord_pivot[1]], pivot_val, x)
            S = transvections(S,i,k,x)
            # for ligne in S : 
            #     print(" ".join(f"{x:5.2f}" for x in ligne))
            # print("\n")
            
        i += 1
    return S

def triangulariser(S) :
    i = 0    
    #print("simplifier(S) :", simplifier(S))
    while(simplifier(S)[0]) :
        #print("test :", simplifier(S))

        S = simplifier(S)[1]
        
        if i >= len(S[1]) - 2 :
            return True, S        
        else : 
            i = i + 1
        S = pivoter(S,i-1)
        for ligne in S : 
            print(" ".join(f"{x:5.2f}" for x in ligne))
        print("\n")
    return False, []


def resoudre(S):
    triangulariser_possible, S = triangulariser(S)
    #print("Matrice triangulaire :\n", S, triangulariser_possible, "\n")
    if triangulariser_possible:
        sol = [0] * len(S[0])
        inconnu = False

        N = np.array(S)
        if sum(N[:,-1]) == 0 :
            inconnu = True
            #sol[-1] = 1
            for i in range(len(S)) :
                S[i] = S[i][:-1]
                S[i][-1] = S[i][-1] * -1
                ## i = i[:-1]
                ## i[-1] = i[-1]*-1
        
        # print("\n")
        # for ligne in S : 
        #     print(" ".join(f"{x:5.2f}" for x in ligne))
        # print("\n")
        # input()


        for i in range(len(S)-1, -1, -1) :
            for j in range(i-1, -1, -1):
                S = transvections(S, j, i, -S[j][i]/S[i][i])
                # print("\n")
                # for ligne in S : 
                #     print(" ".join(f"{x:5.2f}" for x in ligne))
                # print("\n")
                # print("coeff :", -S[j][i]/S[i][i], "\nrep : ", S[i][-1], "\ni :", i, "j :", j, "\n" )
                # input()
            sol[i] = S[i][-1]/S[i][i]
    

        if inconnu :
            for i in range(len(sol)) :
                if sol[i] == 0 :
                    sol[i] = 1
                    break
            


        return sol
    else : 
        return ["Equation absurde trouvé"]
    

#print(resoudre([[1,-1, 1,-1,  2], [0, 2, 1,-3,  1], [0, 0, 0, 4,  3],[0, 0, 5, 5,-10]]))
        
#M = np.load("Exercice_4/Ex4_data/Gaston_Berger/413 avenue Gaston Berger, Aix en Provence, France_Matrice.npy")
M = [   [0.2,   0.88,   0.46,   0.46,   0.46],  
        [0.2,   0.03,   0.03,   0.46,   0.46],  
        [0.2,   0.03,   0.03,   0.03,   0.03],  
        [0.2,   0.03,   0.46,   0.03,   0.03],  
        [0.2,   0.03,   0.03,   0.03,   0.03]] #modif attention, les gars

# M = [[0.5, 0.5, 0],
#      [0.3, 0.3, 1],
#      [0.2, 0.2, 0]]  
In = np.identity(len(M))
a = np.array(M)
test = In - a

# determinant = np.linalg.det(test)
# print("Déterminant :", determinant)

test = test.tolist()

for i in range(len(test)):
    test[i].append(0)
    print(test[i])
print("\n")    


    
# somme_colonnes = [sum(colonne) for colonne in zip(*M)]
# print("somme col :",somme_colonnes)

# test = np.array(test)
# test[-1,:] = 1
# test.tolist()



r = resoudre(test)
print("Solution :", r)

r = r[0:-1]
r = np.array(r)
print(a @ r)

print(r/r.sum())