"""
Sample list of numbers

Exercise 1: Filter even numbers using a lambda function

"""

lista = ["a", "b", 10, 20, 345, "test", 890, "24"]

filter = list(filter(lambda x: isinstance(x, (int, float)), lista))

print(f"Numbers: {filter}")