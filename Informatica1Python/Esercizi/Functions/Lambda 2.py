"""
Exercise 2: Filter numbers greater than 5 using a lambda function
"""


lista = [1, 2, 10, 20, 345, 0, 890, 24, 5]

numbers = list(filter(lambda x: x > 5, lista))


print(f"Numbers greater than 5: {numbers} ")
