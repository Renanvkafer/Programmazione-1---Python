"""
Date due matrici:

Creare un vettore che contenga la somma degli elementi di ogni riga di A e di B, senza usare le funzioni di numpy, considerando che le due matrici hanno le stesse dimensioni

"""

import numpy as np
A = np.random.randint(0, 2, (3, 3))
B = np.random.randint(0, 2, (3, 3))

Sum = np.array([])
SumAux = 0

print("Matrice A:\n", A, "\n")
print("Matrice B:\n", B)


for i in range (len(A)):
        for j in range (len(A)):
            SumAux += A[i][j] + B[i][j]

        Sum = np.append(Sum, SumAux)
        SumAux = 0


print("\nSomma \n", Sum)


#Ripetere l'esercizio considerando che le due matrici hanno dimensioni diverse
A1 = np.random.randint(0, 2, (2, 3))
B1 = np.random.randint(0, 2, (3, 3))

Sum1 = np.array([])
SumAux1 = 0

print("Matrice A1:\n", A1, "\n")
print("Matrice B1:\n", B1)

for i in range (len(B1)):
        for j in range (len(A1)):
            SumAux1 += A1[i][j] + B1[i][j]

        Sum1 = np.append(Sum, SumAux1)
        SumAux1 = 0

print("\nSomma \n", Sum1)



