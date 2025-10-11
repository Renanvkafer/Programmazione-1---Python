"""
Part 1: Name Binding

Create two variables, a and b, and assign the value "Hello" to a and 5 to b.
Print the values of a and b.
Now, reassign the value "World" to a
Print the values of a and b again.
Explain the changes you observe and discuss the concept of name binding.


Part 2: Type Conversion

Create a variable x and assign the value "10" to it (as a string).
Create another variable y and assign the value 5 to it (as an integer).
Attempt to add x and y together using the + operator.
Discuss the outcome, and explain why it happened.
Convert x to an integer using the int() function and store the result in a new variable x_int.
Now, try adding x_int and y together.
Discuss the outcome, and explain how type conversion resolved the issue.


"""

a = "Hello"
b = 5

print(f"A: {a}\nB: {b}")

a = "World"

print(f"A: {a}")

x = "10"
y = 5

print(f"Result: a + b - can only concatenate str (not int) to str")

"""Non possiamo farlo con un int e una stringa, perché solleva un TypeError"""

x = int(x)

z = x + y

print(f"Result: {z}")

"""Adesso possiamo farlo perché  é una operazione di int + int """
