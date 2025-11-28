"""
Data una matrice si scriva un algoritmo per stabilire se la somma degli elementi della diagonale principale è il doppio della somma degli elementi sulla diagonale secondaria. Soluzione: Le due somme sono accumulate nelle variabili P,S. Le somme si ottengono scandendo le diagonali con l’unico indice i. Infine, all’uscita del ciclo si controlla la proprietà.

"""

import numpy as np

matrice = np.array([[2, 0, 4],
              [0, 2, 0],
              [4, 0, 1],])
P = 0
S = 0



for i in range(len(matrice)):
        P += matrice[i][i]
        S += matrice[i, len(matrice) - 1 - i]

def isdouble(A, B):
    if A * 2 == B:
        return True
    return False

a = isdouble(P, S)

print("\n", matrice, "\n")
print(P, "\n")
print(S, "\n")

if a:
    print("\ndegli elementi della diagonale principale è il doppio della somma degli elementi sulla diagonale secondaria")
else:
    print("\ndegli elementi della diagonale principale NON è il doppio della somma degli elementi sulla diagonale secondaria\n")


