"""
Definiamo due matrici


A = np.matrix([[-1,3,0], [1,0,2]]) # prima matrice
B = np.matrix([[5,2], [7,1], [1,2]]) # seconda matrice
Calcolare il prodotto matriciale tra le due matrici (senza le funzioni di numpy)
Sia A∈Rm,p, B∈Rp,n, e C∈Rm,n. La definizione del prodotto riga-colonna può essere espresso come:

cij=aiκbκj

Un elemento di C corrisponde alla molteplicazione tra una riga di A e una colonna di B. L'indice κ serve a scorrere le posizioni delle righe di A e le colonne di B.

Inizializzare C con le dimensioni corrette, prendendole da A e B
Scrivere in una funzione
Provare con diverse matrici con dimensione 2x4 e 4x3

Fare lo stesso utilizzando le funzioni di numpy

Calcolare il prodotto punto-punto tra due matrici (senza le funzioni di numpy)

Fare lo stesso utilizzando le liste

Calcolalo con numpy

"""
import numpy as np

A = np.array([
    [-1,3,0],
    [1,0,2]])
B = np.array([
    [5,2],
    [7,1],
    [1,2]])


matrix_produtto = np.array([])
aux_produtto = 0
aux_aux = 0


for i in range(len(B) - 1):
    for j in range(len(B) - 1):
          for b in range(len(A) + 1):
                aux_aux = A[i][b] * B[b][j]
                aux_produtto = aux_aux + aux_produtto
          matrix_produtto = np.append(matrix_produtto, aux_produtto)
          aux_produtto = 0


matrix_produtto = matrix_produtto.reshape(2, 2)
print(matrix_produtto)

def produtto_matrice (matrice1, matrice2):
    matrix_produtto_func = np.array([])
    aux_produtto_func = 0

    for f in range(len(matrice1)):
        for l in range(len(matrice2[0])):
            for x in range(len(matrice2)):
                aux_aux_func = matrice1[f][x] * matrice2[x][l]
                aux_produtto_func = aux_aux_func + aux_produtto_func
            matrix_produtto_func = np.append(matrix_produtto_func, aux_produtto_func)
            aux_produtto_func = 0
    matrix_produtto_func = matrix_produtto_func.reshape(len(matrice1), len(matrice2[0]))

    return matrix_produtto_func



a = produtto_matrice(A, B)
print("\n", a)

A1 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
B1 = np.array([
    [1, 0, 2],
    [0, 1, 3],
    [1, 0, 0],
    [2, 1, 1]
])

AB = produtto_matrice(A1, B1)
print("\nExemplo 1:\n", AB, "\n")


A2 = np.array([
    [-1, 0, 2, 1],
    [3, -2, 0, 4]
])
B2 = np.array([
    [2, -1, 0],
    [1, 3, 2],
    [0, 4, -2],
    [-2, 1, 1]
])

AB1 = produtto_matrice(A2, B2)
print("Exemplo 2:\n", AB1, "\n")


A3 = np.array([
    [0, 2, -1, 3],
    [1, 1, 0, -2]
])
B3 = np.array([
    [2, 1, 0],
    [-1, 0, 2],
    [0, -2, 1],
    [1, 3, -1]
])

AB2 = produtto_matrice(A3, B3)
print("Exemplo 3:\n", AB2, "\n")



