"""
Analyze your monthly expense...

Create a Numpy array named expenses to represent your monthly expenses for the last year. The array should contain 12 elements, each representing your monthly expenses for January to December. You can use random values to simulate expenses.

Calculate and print the following information:

Total expenses for the year.
Average monthly expenses.
The highest monthly expense and its corresponding month (e.g., "Month 3:  XXX").−Thelowestmonthlyexpenseanditscorrespondingmonth(e.g.,"Month7: XXX").

Slice the expenses array to create a new array named first_half that contains expenses for the first 6 months (January to June) and a new array named second_half that contains expenses for the last 6 months (July to December).

Calculate and print the following information for the first half-year:

Total expenses.
Average monthly expenses.
The highest monthly expense and its corresponding month.
The lowest monthly expense and its corresponding month.

Reshape the expenses array into a 3x4 matrix, where each row represents a quarter of the year (3 months). Print the reshaped matrix.

"""

import random

monthly = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
           "December"]

expenses = random.sample(range(1200, 3000), 12)

total_expenses = sum(expenses)

print(f"Expenses {expenses}\nTotal Expense {total_expenses}")

highest_monthly = 0
list_aux = []
monthly_high = ""

for i in range(len(expenses)):
    if expenses[i] > highest_monthly:
        highest_monthly = expenses[i]
        monthly_high = monthly[i]

list_aux.append(f"{monthly_high} - {highest_monthly}")
print(list_aux)

first_half = []
last_half = []

for i in range(len(expenses)):
    if i < int(len(expenses) / 2):
        first_half.append(expenses[i])
    else:
        last_half.append(expenses[i])

print(f"First half {first_half}\nLast half {last_half}")

highest_firstHalf = 0
lowest_firstHalf = expenses[0]
aux_mes = ""
aux_mes_lowest = ""

for i in range(len(first_half)):
    if first_half[i] > highest_firstHalf:
        highest_firstHalf = expenses[i]
        aux_mes = monthly[i]

for i in range(len(first_half)):
    if first_half[i] < lowest_firstHalf:
        lowest_firstHalf = expenses[i]
        aux_mes_lowest = monthly[i]

print(f"\nFirst Half\nHighest - {aux_mes} - {highest_firstHalf}\nLowest - {aux_mes_lowest} - {lowest_firstHalf}")

highest_lastHalf = 0
lowest_lastHalf = expenses[6]
aux_mesLast = ""
aux_mes_lowestLast = ""

for i in range(len(last_half)):
    if last_half[i] > highest_lastHalf:
        highest_lastHalf = expenses[i + 6]
        aux_mesLast = monthly[i + 6]

for i in range(len(last_half)):
    if last_half[i] < lowest_lastHalf:
        lowest_lastHalf = expenses[i + 6]
        aux_mes_lowestLast = monthly[i + 6]

print(f"\nLast Half\nHighest - {aux_mesLast} - {highest_lastHalf}\nLowest - {aux_mes_lowestLast} - {lowest_lastHalf}\n")

rows = 4
cols = 3

lista_3x4 = [expenses[i * cols:(i + 1) * cols] for i in range(rows)]

for i in lista_3x4:
    print(" ".join(f"[{x}]" for x in i))