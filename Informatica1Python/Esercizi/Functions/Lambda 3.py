"""
Exercise 3: Square each number using a lambda function and map
"""


lista = [10, 2, 3, 20, 100, 1000]

numbers = map(lambda x: x ** 2, lista)

print(f"Square numbers: ", list(numbers))