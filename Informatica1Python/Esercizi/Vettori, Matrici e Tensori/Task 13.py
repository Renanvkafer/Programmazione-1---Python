"""
Dato il cubo precedentemente definito, trovarne il valore medio, senza usare le funzioni di numpy

Sostituire i valori del cubo maggiori di 3 con il suo valore medio


"""

import numpy as np

cubo = np.random.randint(0, 12, (3, 3, 3))

print("Cubo:\n", cubo)

flat = cubo.flatten()

for i in range(len(flat)):
    for j in range(len(flat)):
        if flat[i] < flat[j]:
            flat[i], flat[j] = flat[j], flat[i]

elemento_med = flat[len(flat)//2]

print("Elemento medio:\n", elemento_med)


for i in range(len(cubo)):
    for j in range(len(cubo)):
        for k in range(len(cubo)):
            if cubo[i][j][k] > 3:
                cubo[i][j][k] = elemento_med

print("Cubo Modificato con la media:\n", cubo)