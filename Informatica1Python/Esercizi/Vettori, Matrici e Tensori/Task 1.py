"""

Questa sezione contiene una serie di esercizi riguardo l'utilizzo di liste, matrici e tensori.

Contare i numeri pari nella lista

Selezionare e contare i numeri dispari nella lista

Trovare il massimo e il minimo nella lista (senza usare le funzioni max e min)

Dati tre vettori calcolarne l'intersezione (non usare le funzioni build-in di python)

Dati tre vettori calcolarne l'unione eliminando i duplicati (non usare le funzioni build-in di python)

Fare lo stesso utilizzando i set

Dati due vettori calcolarne l'intersezione e ordinarla (non usare le funzioni build-in di python)

"""

import numpy as np

lista = np.random.randint(1, 100, 10)
print(lista)

count_pari = 0
count_dispari = 0


for i in range(len(lista)):
    if lista[i] % 2 == 0:
        count_pari += 1
    else:
        count_dispari += 1

print(f"Pari: {count_pari}\nDispari: {count_dispari}")


min_num = lista[0]
max_num = 0

for i in range(len(lista)):
    if max_num < lista[i]:
       max_num = lista[i]

print(f"Max: {max_num}")

for i in range(len(lista)):
    if min_num > lista[i]:
        min_num = lista[i]

print(f"Min: {min_num}")


vet1 = [10, 20, 30, 23, 50, 66]
vet2 = [10, 33, 23, 15, 50, 20]
vet3 = [10, 23, 90, 20, 22, 50]


vet_intersezione = []
vet_unione = []


for i in range(len(vet3)):
    for j in range(len(vet1)):
        for p in range(len(vet2)):
            if vet1[i] == vet2[j] == vet3[p]:
                vet_intersezione.append(vet1[i])

print(f"Intersezione: {vet_intersezione}")

for i in range(len(vet3)):
    if vet1[i] not in vet_unione:
        vet_unione.append(vet1[i])
    if vet2[i] not in vet_unione:
        vet_unione.append(vet2[i])
    if vet3[i] not in vet_unione:
        vet_unione.append(vet3[i])


print(f"Unione: {vet_unione}")


vet5 = [23, 11, 9, 50, 42, 13]
vet4 = [13, 42, 50, 9, 77, 88]


vet_intersezione_ordinato = []


for i in range(len(vet3)):
    for j in range(len(vet1)):
        if vet4[i] == vet5[j]:
           vet_intersezione_ordinato.append(vet4[i])

print(f"Intersezione 2 vettori: {vet_intersezione_ordinato}")

for i in range(len(vet_intersezione_ordinato)):
    for a in range(len(vet_intersezione_ordinato)):
       if vet_intersezione_ordinato[i] < vet_intersezione_ordinato[a]:
           vet_intersezione_ordinato[i], vet_intersezione_ordinato[a] = vet_intersezione_ordinato[a], vet_intersezione_ordinato[i]

print(f"Intersezione ordinata: {vet_intersezione_ordinato}")
