"""In this exercise, create four functions (add, subtract, multiply, and divide) to perform basic arithmetic
operations. Create a main calculator function that takes user input for the operation they want to perform and the
two numbers on which the operation should be applied. The selected function is then called to perform the calculation
and display the result."""

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

ope = int(input("Choose arithmetic operations.:\n"
                " press 1 - Add\n"
                " press 2 - Subtract\n"
                " press 3 - Multiply\n"
                " press 4 - Divide\n \n "))


def arithmetic_operations(a, b):
    if ope == 1:
        return a + b
    if ope == 2:
        return a - b
    if ope == 3:
        return a * b
    if ope == 4:
        return a / b


final_result = arithmetic_operations(number1, number2)

print(f"\nFinal result: {final_result}")
