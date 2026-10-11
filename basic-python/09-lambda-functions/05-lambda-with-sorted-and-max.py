# Lambda with sorted() and max()
# Lambdas shine when passed directly to functions that expect another function.

students = [
    {"name": "Aryan", "marks": 88},
    {"name": "Priya", "marks": 95},
    {"name": "Rahul", "marks": 72},
]

# sorted() needs to know HOW to sort.
# The key argument takes a lambda that returns the value to sort by.
ranked = sorted(students, key=lambda student: student["marks"], reverse=True)

print("Students ranked by marks:")
for student in ranked:
    print(student["name"], "-", student["marks"])

# max() and min() work the same way
topper = max(students, key=lambda student: student["marks"])
print("Topper:", topper["name"], "with", topper["marks"], "marks")

# Without a lambda, sorted() would compare dictionaries directly,
# which is not what we want. The lambda tells Python exactly which
# value to look at when sorting.
