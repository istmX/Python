# Dictionary Comprehensions
# Build dictionaries in one line with {key: value for ...}

# Map each name to its length
names = ["Aryan", "Priya", "Rahul"]
name_lengths = {name: len(name) for name in names}
print("Name lengths:", name_lengths)

# Square each number: value -> its square
squares = {n: n * n for n in range(1, 6)}
print("Squares dict:", squares)

# With a condition: only include passing marks
marks = {"Aryan": 88, "Priya": 95, "Rahul": 30, "Sneha": 45}
passing = {name: score for name, score in marks.items() if score >= 40}
print("Passing students:", passing)

# Transform values: convert marks to grades
grades = {
    name: ("pass" if score >= 40 else "fail")
    for name, score in marks.items()
}
print("Grades:", grades)

# Note the syntax difference from lists:
#   lists:  [ expression for item in items ]
#   dicts:  { key: value for item in items }
