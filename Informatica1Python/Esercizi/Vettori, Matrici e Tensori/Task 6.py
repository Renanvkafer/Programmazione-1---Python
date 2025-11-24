"""
Data la seguente matrice:

Sommare gli elementi sulla diagonale principale e secondaria con un unico ciclo for


"""

import numpy as np
matrice = np.random.randint(1, 10, (10, 10))

aux_arra = 0
SumTotalPrimaria = 0
SumTotalSecondary = 0
j = 0
print(matrice, "\n")


for i in range(len(matrice)):
        SumTotalPrimaria += matrice[i, i]
        SumTotalSecondary += matrice[i, len(matrice) - 1 - i]


print(SumTotalPrimaria, "\n")
print(SumTotalSecondary, "\n")

