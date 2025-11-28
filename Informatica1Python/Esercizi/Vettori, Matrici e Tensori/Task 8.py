"""

Dato un cubo di dimensione 4x4x4 come il seguente:

calcolare la somma degli elementi che hanno valore maggiore di 2 e minore di 4, senza usare le funzioni di numpy

"""
import numpy as np

cubo = np.random.randint(0, 5, (4, 4, 4))

SumMag = 0

print("Cubo:\n", cubo)

for i in range(len(cubo)):
    for j in range(len(cubo)):
        for k in range(len(cubo)):
            if 2 < cubo[i][j][k] < 4:
                SumMag += cubo[i][j][k]

print("\nSomma Maggiore di 2 e minore di 4: ", SumMag)


#Dato un vettore di dimensione n e numero x reale scrivere un algoritmo per stabilire se esistono in U almeno due elementi u1,u2 tali che u1+u2=x
vet = [1, 10, 20, 30]
x = 40


def essiste_x(a, b):
    for i1 in range(len(vet)):
        for j2 in range(len(vet)):
            if a[i1] + a[j2] == b:
                return True
    return False

result = essiste_x(vet, x)
if result:
    print("\nEssiste X: ", result, x)
else:
    print("\nNon Essiste X: ", result, x)


matrice = np.random.randint(0, 2, (3, 3))

teste = np.array([[3, 0, 0, 0],
              [0, 4, 0, 0],
              [0, 0, 10, 0],
              [0, 0, 0, 0]])

print("\nNatrice\n", matrice)

def matrice_diagonale(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if i == j:
                break
            if matrice[i][j] != 0:
                return False
    return True

result1 = matrice_diagonale(teste)
if result1:
   print("\nÉ diagonale\n", teste)
else:
   print("\nNon é diagonale:\n ", teste)



