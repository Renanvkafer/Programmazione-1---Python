"""
Scoprire se la diagonale primaria è nulla: una matrice ha diagonale nulla se tutti gli elementi della diagonale principale sono nulli.

Scoprire se sia la diagonale primaria che la secondaria sono entrant nulle

TIP: per accedere alla diagonale secondaria, invertire l'ordine degli indici

Ripetere l'esercizio utilizzado un ciclo while invece del for


Inserire il calcolo in un funzione che restituisca True se la matrice è nulla, False altrimenti e provare per diverse matrici

"""

import numpy as np

A = np.array([[0, 3, 3, 0],
              [-8, 0, 0, 4],
              [-1, 0, 0, 6],
              [1, 9, -9, 0]])

diagonale_prima = np.array([])

aux_metta = 0


for i in range(len(A)):
    for j in range(len(A)):
        if j == aux_metta:
            diagonale_prima = np.append(diagonale_prima, A[i][j])
    aux_metta += 1


aux_diago = 0

for i in range(len(diagonale_prima)):
    if diagonale_prima[i] == 0:
        aux_diago = 1
    else:
        aux_diago = 2
        break

if aux_diago == 1:
    print(f"La diagonale prima é nulla {diagonale_prima}")
else:
    print(f"La diagonale prima non é nulla {diagonale_prima}")

print(f"\nMatrice inteira:\n"
      f" {A}")


aux_metta_inv_i = 0
aux_metta_inv_j = 0

aux_len = int(len(A)) - 1


B = np.array([])

for i in range(len(A)):
    for j in range(len(A)):
        B = np.append(B, A[aux_len -  aux_metta_inv_i][aux_len - aux_metta_inv_j])
        aux_metta_inv_j += 1
    aux_metta_inv_i += 1
    aux_metta_inv_j = 0

B = B.reshape(len(A), len(A))

print(f"\nMatrice inversa:\n"
      f" {B}\n")



diagonale_secondaria = np.array([])

aux_metta_secondaria = 0


for i in range(len(A)):
    for j in range(len(A)):
        if j == aux_metta_secondaria:
            diagonale_secondaria = np.append(diagonale_secondaria, A[i][j])
    aux_metta += 1


aux_diago_secondaria = 0

for i in range(len(diagonale_secondaria)):
    if diagonale_secondaria[i] == 0:
        aux_diago_secondaria = 1
    else:
        aux_diago_secondaria = 2
        break

if aux_diago_secondaria == 1:
    print(f"La diagonale secondaria é nulla {diagonale_secondaria}")
else:
    print(f"La diagonale secondaria non é nulla {diagonale_secondaria}")

print(f"\nMatrice inteira:\n"
      f" {B}")




def trovare_matrice_nulla (matrice):
    aux_metta_function = 0
    diagonale_prima_test = np.array([])
    for a in range(len(matrice)):
        for b in range(len(matrice)):
            if b == aux_metta_function:
                diagonale_prima_test = np.append(diagonale_prima_test, matrice[a][b])
        aux_metta_function += 1

    aux_diago_func = 0

    print(f"\nMatrice:\n"
          f"{diagonale_prima_test}\n")

    for a in range(len(matrice)):
        if diagonale_prima_test[i] == 0:
            aux_diago_func = 1
        else:
            aux_diago_func = 2
            break
    if aux_diago_func == 1:
        return True
    else:
        return False


matrix = np.array(
              [[0, 2, 13, 0],
              [-23, 0, 0, 89],
              [-28, 0, 0, 102],
              [1, 9, -323, 0]])


if trovare_matrice_nulla(matrix):
    print("Matrice nulla\n", matrix)
else:
    print("Matrice non nulla\n", matrix)





