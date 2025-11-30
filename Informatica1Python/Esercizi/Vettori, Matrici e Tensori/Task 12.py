"""
Creare una matrice i cui valori sono il risultato della somma pesata dei punti delle due matrici. Con peso 0.3 per la prima e 0.7 per la seconda.

Convertire in float per poter avere i valori corretti. la sintassi è: variabile = variabile.astype(float32)

"""

import numpy as np

matrice1 = np.random.randint(0, 99, (4, 4))

matrice2 = np.random.randint(0, 99, (4, 4))

matriceSomma = np.array([])
aux = 0

print(matrice1, "\n")
print(matrice2, "\n")

for i in range(len(matrice1)):
    for j in range(len(matrice1)):
        a = (matrice1[i][j] * 0.3)
        b = (matrice2[i][j] * 0.7)
        print("A:\n", a), print("B:\n", b)
        matriceSomma = np.append(matriceSomma, a + b )


print("Matrice 1:\n", matrice1)
print("Matrice 2:\n", matrice2)

matriceSomma = np.reshape(matriceSomma, (4, 4))

print("Matrice Somma:\n", matriceSomma)

matriceSomma = matriceSomma.astype('float32')

print("Matrice Somma float32:\n",matriceSomma)