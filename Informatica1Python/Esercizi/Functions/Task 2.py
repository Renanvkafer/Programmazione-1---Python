"""
Create a program that calculates the factorial of a number using a recursive function.

Create a function that takes a number as an argument and returns the factorial of the number.

Call the function and display the result.
"""


number = int(input("Enter a number: "))


def factorial_calc(a):
    result_factorial = 1
    for i in range(1, a + 1):
        result_factorial *= i

    return result_factorial


result = factorial_calc(number)

print(f"\nFactorial number result: {result}")
