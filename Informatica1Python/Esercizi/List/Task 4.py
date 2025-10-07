"""
Create a list with the words: apple, banana, cherry, date, elderberry.

Using enumerate to create a list of index-word tuples:

Print each number in the list with its index

Using slicing and indexing to extract the third and fourth elements:

Check if the word banana is in the list of words:

Find the shortest and longest words in the list: Hint: the min and max functions can take a key argument that is a function to be applied to each element of the list before comparison.

Append a new word to the list of words:

"""

lista = ["apple", "banana", "cherry", "date", "elderberry"]

lista_index = enumerate(lista)

print(f"Tuple index-words: ", list(lista_index))

lista_3_4_elements = [lista[3], lista[4]]

print(list(lista_3_4_elements))


def check_banana(banana_list):
    return "banana" in banana_list


a = check_banana(lista)

print(f"banana is in the list of words: {a}")


append_list = lista

append_list.append("new")

print(f"New item append: {append_list}")

b = len(lista[0])

print(b)

shortest = len(lista[0])
shortest_word = lista[0]

for i in range(len(lista)):
    if len(lista[i]) <= shortest:
        shortest_word = lista[i]


print(f"shortest word: {shortest_word}")


longest = len(lista[0])
longest_word = lista[0]

for i in range(len(lista)):
    if len(lista[i]) >= shortest:
        longest_word = lista[i]


print(f"longest word: {longest_word}")