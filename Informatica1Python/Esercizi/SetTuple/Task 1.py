"""
Create two sets, set1 and set2, with some elements of your choice.
Find the union of set1 and set2 and store it in a variable called union_set.

Find the intersection of set1 and set2 and store it in a variable called intersection_set.

Create a new set, set3, which contains elements that are in set1 but not in set2.

Create a new set, set4, which contains elements that are in set2 but not in set1.

"""

set1 = {10, 20, 30, 40, "element 2"}
set2 = {10, 20, 123, "element 1"}

union_set = tuple(set(set1).union(set2))

print(f"Union: {union_set}")

intersection_set = tuple(set(set1).intersection(set2))

print(f"Intersections: {intersection_set}")

set3 = {30, "element 2", 89, 100}

set4 = {123, "element 1", 1432, 122}

