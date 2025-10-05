"""
Write a Python program that converts temperatures between Celsius and Fahrenheit based on user input.

Ask the user to choose the conversion direction: Celsius to Fahrenheit or Fahrenheit to Celsius.

Ask the user to enter a temperature value.

Use an if statement to perform the conversion based on the chosen direction.
HINT: Fahrenheit = (temperature * 9/5) + 32 and Celsius = (temperature - 32) * 5/9

Print only the first 3 decimal. HINT: use the format print(f"string{variable:.3f})

In a single line assign to a variable the value "Celsius" if the user selected Celsius and "Fahrenheit" otherwise.
HINT the syntax is variable = value1 if condition else value 2
"""

conv = int(input("Choose the conversion direction:\n"
                 " press 1 - Celsius to Fahrenheit\n"
                 " press 2 - Fahrenheit to Celsius\n \n "))

temp = int(input("\nenter a temperature value: "))


def convert_temp(temperature, conversion):
    if conv == 1:
        result = temp * 9/5 + 32
        convert = "Fahrenheit"
    else:
        result = (temp - 32) * 5 / 9
        convert = "Celsius"

    return result, convert


final_temp, conv_temp = convert_temp(temp, conv)

print(f"\n{final_temp:.3f}")
print(f"Temperature: {conv_temp}")
