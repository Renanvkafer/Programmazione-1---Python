"""

Data la seguente stringa: "avorp id agnirts anu è atseuq", stampare la stringa al contrario saltando gli spazzi

Cercare nella stringa la seguente sottostringa "id" se presente stampare la posizione in cui si trova

Eliminare gli spazzi dalla stringa senza usare funzioni di libreria

Data una stringa, creare una funzione che verifica se la stringa è palindroma

Fare lo stesso con la seguente stringa: "a valle tra masse ebre la nera l'accesa d'ira etna ti moveva; l'etna gigante lave vomitante arida secca l'arena l'erbe essa martellava". Ignorare la punteggiatura e gli spazzi

"""


import re

stringa = "avorp id agnirts anu è atseuq"

stringa = stringa[::-1]

print(stringa)

a = stringa.find("di")

print("Posizione di:", a, a + 1)

stringa = stringa.replace(" ", "")

print("Stringa senza spazzi", stringa)


def palindroma(strin): ##dobbiamo anche formatare la stringa :)
    aux_string = strin.replace(" ", "")
    aux_string = aux_string.lower()
    aux_string = re.sub('[^a-z0-9]', '', aux_string)
    strin = strin.replace(" ", "")[::-1]
    strin = strin.lower()
    strin = re.sub('[^a-z0-9]', '', strin)
    return strin == aux_string

frase = "a valle tra masse ebre la nera l'accesa d'ira etna ti moveva; l'etna gigante lave vomitante arida secca l'arena l'erbe essa martellava"


if palindroma(frase):
    print("\nQuesta stringa é una palindroma:\n", frase)
else:
    print("\nQuesta stringa non é una palindroma:\n", frase)

teste = "renan sabe das coisas"

b = palindroma(teste)
c = palindroma(frase)

print("\n",b, "\n")
print("\n",c)