"""
Exercise: Calculating Expenses and Finding Savings
Imagine you and your friends are planning a road trip, and you want to keep track of your expenses to ensure everyone pays their fair share. Create a Python program to help you manage your expenses and find potential savings.

Create a list of names to represent each person in your group:

Create a list of lists to represent expenses for each person during the road trip. Each inner list corresponds to an individual's expenses:

Calculate the total expenses for each person and store them in a separate list. HINT the sum function can be used to calculate the sum of a list of numbers

Calculate the average expenses for the entire group:

Identify individuals who spent more than the average and those who spent less:

Calculate how much each person needs to pay or save to balance expenses:

Print the results to see who needs to contribute more and who can expect some savings:

"""

lista_names = ["Jorge", "Renan", "Enzo", "Victor", "Amanda", "Maria Fernanda"]

lista_expenses = [
    [34, 80, 34, 12, 99, 112],
    [15, 24, 9, 67, 13.70, 119.90],
    [13.25, 17, 22, 43, 23, 56.90],
    [11.33, 98, 10, 12.75, 10, 123],
    [2.30, 35, 60, 110, 5.24, 87.22],
    [8.70, 12, 7.50, 81, 34, 99],
]

total_person = []

for i in range(len(lista_expenses)):
    soma = 0
    for j in range(len(lista_expenses)):
        soma += lista_expenses[i][j]
    total_person.append(soma)

print(total_person)

total = (sum(total_person)) / len(total_person)

print(f"Total average Group: {total}")

spend_more = []
spend_less = []

for i in range(len(total_person)):
    if total_person[i] < total:
        spend_more.append(lista_names[i])
    else:
        spend_less.append(lista_names[i])

print(f"Individuals who spent more: {spend_more}  -  Those who spent less: {spend_less}")

save_or_contribute = []
a = []

for i in range(len(total_person)):
    a.append(total_person[i] - total)
    if a[i] > 0:
        save_or_contribute.append(f"{lista_names[i]} - {a[i]:.2f} - expect some savings ")
    else:
        save_or_contribute.append(f"{lista_names[i]} - {abs(a[i]):.2f} - needs to contribute more")

print(f"who needs to contribute more and who can expect some savings: {save_or_contribute}")
