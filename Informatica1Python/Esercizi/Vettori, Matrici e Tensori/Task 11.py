"""
Creare una lista di 4 elementi

Trasformare la lista in una matrice 4x4 (definendola tramite liste di sottoliste): ogni riga della matrice è definita dalla lista iniziale

Trasformare la matrice in un cubo 4,4,4 in cui ogni strato è definito dalla matrice iniziale


Convertire matrice e cubo in np.array e verificarne le dimensioni

Data la matrice, calcolare la sua trasposta

Creare una funzione per aggiungere una colonna di 1 ad entrambe le matrici in modo da avere dimensioni 4x5

Creare una matrice i cui valori sono il risultato della somma pesata dei punti delle due matrici. Con peso 0.3 per la prima e 0.7 per la seconda.

Convertire in float per poter avere i valori corretti. la sintassi è: variabile = variabile.astype(float32)

"""

import numpy as np

l = [1,2,3,4]
matrice = np.array([l,l,l,l])
print("Lista: ",l, "\n")

print("La lista adesso é una matrice 4x4:\n",matrice)



cubo = np.array([
    [l,l,l,l],
    [l,l,l,l],
    [l,l,l,l],
    [l,l,l,l],
])


print("La matrice adesso é un cubo:\n",cubo)


print("\nDimensione matrice:\n",matrice.shape, "\nDimensione cubo:\n", cubo.shape)


matrici = np.random.randint(1, 4, (3, 2))

print("\nMatrice Nova:\n",matrici)

matrici_composta = np.array([])

matrici_compostaA = matrici.T #Possiamo fare cosi anche


for i in range(len(matrici[0])):
    for j in range(len(matrici)):
        matrici_composta = np.append(matrici_composta,matrici[j][i])


print("\nMatrice Transposta:\n", matrici_compostaA)



print("\nMatrice Resize:\n", matrice)

def add_riga(m):
    mt = np.array([
        [1],
        [1],
        [1],
        [1],
    ])
    m = np.column_stack((m, mt)) #come un shift a destra (non é come un shift hahaha :\ )

    #possiamo fare anche a sinistra m = np.column_stack((mt, m)) l'inverso oppure np.hstack((mt, m)) sarebbe la stessa cosa

    return m


testi = add_riga(matrice)
print("\nMatrice 4X5:\n", testi)
print("\nShape\n", testi.shape)



