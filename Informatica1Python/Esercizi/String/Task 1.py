"""
Create a variable my_string and assign it the value "Hello, Python!".
Print the length of my_string.
Print the first character of my_string.
Print the last character of my_string.
Check if the word "Python" is present in my_string. Print the result as a boolean value.
"""

a = "Hello, Python!"


def check_python(string):
    return "Python" in string


print(len(a))
print(a[0:1])
print(a[13:14])

print(check_python(a))
