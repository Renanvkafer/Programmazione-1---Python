"""
Exercise 5: Sort numbers in descending order using a lambda function
"""

lista = [10, 1, 0, 23, 100, 34, 3, 5]


lista.sort(key=lambda num: num, reverse=True)

print(lista)