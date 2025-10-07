"""
Create a list with the square of each number in the range

Using list comprehension to square each number in the range:

Use list comprehension to triple each number:

Find the minimum, maximum values in the list:

"""

lista = [20, 40, 80, 3, 2, 15, 150]

square_list = list(map(lambda x: x ** 2, lista))

print(square_list)

triple_list = list(map(lambda x: x * 3, square_list))

print(triple_list)

"""
minimum
"""

minimum = lista[0]
max_number = lista[0]

for i in range(len(lista)):
    if lista[i] < minimum:
        minimum = lista[i]


print(f"minimum {minimum}")

"""
max
"""

for i in range(len(lista)):
    if lista[i] > max_number:
        max_number = lista[i]

print(f"max {max_number}")

