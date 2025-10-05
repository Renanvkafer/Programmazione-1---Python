"""
Exercise: Calculate the Sum of Even Numbers

Write a Python program that calculates the sum of even numbers within a given range.

Ask the user to enter a positive integer as the upper limit of the range.

Use a for loop to iterate through numbers from 1 to the user-specified upper limit.
Inside the loop, use an if statement to check if each number is even (i.e., divisible by 2).
If the number is even, add it to a running sum.

Print the sum of even number and the upper limit
"""

pari = 0

number = int(input("enter a positive number (that's the range): "))


for i in range(number + 1):
    if i % 2 == 0:
        pari += 1


print("upper limit ", number)
print(pari)
