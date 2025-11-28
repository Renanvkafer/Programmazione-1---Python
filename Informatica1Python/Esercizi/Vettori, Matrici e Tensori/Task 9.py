"""
Data una stringa composta da caratteri dell’alfabeto della lingua italiana scrivere un algoritmo per contare il numero di doppie che contiene la stringa

Data una matrice si scriva un algoritmo per stabilire se la somma degli elementi della diagonale principale è il doppio della somma degli elementi sulla diagonale secondaria. Soluzione: Le due somme sono accumulate nelle variabili P,S. Le somme si ottengono scandendo le diagonali con l’unico indice i. Infine, all’uscita del ciclo si controlla la proprietà.

"""

stringa = "Matrice italiana della lingua latina"
stringa_doppie = []
count_string  = []
countaux = 0

for i in range(len(stringa)):
    for j in range(len(stringa)):
        if stringa[i] == stringa[j] and stringa[i] != " ":
                 countaux += 1
                 if stringa[i] not in stringa_doppie:
                     stringa_doppie.append(stringa[i])

    if len(stringa_doppie) != len(count_string):
        count_string.append(countaux)
    countaux = 0

print(stringa_doppie)
print("\n", count_string)


