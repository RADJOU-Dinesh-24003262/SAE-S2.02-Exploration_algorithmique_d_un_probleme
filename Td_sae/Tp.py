import numpy as np

def norme(X) : 
    somme_carr = 0
    for i in X : 
        somme_carr += i**2
    return somme_carr**0.5

def plus_grnd_val_propre(A, taille, e = 10**(-10)) :
    #X_new = np.array([np.random.rand()]*taille)
    X_new = np.random.rand(taille)

    X_old = np.zeros(taille)

    while norme(X_new - X_old) > e:
        X_old = X_new
        temp = A @ X_old
        X_new = temp/norme(temp)
    X = X_new
    print("valeur propre :", norme(A @ X))


x = np.array([3,4])
print(norme(x))
 
X1 = np.array([[2, 3],[1, 0]])
plus_grnd_val_propre(X1, 2)