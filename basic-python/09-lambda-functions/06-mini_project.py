# Mini Project: Grade Analyzer
# This project uses lambda functions to process student marks.

# Each student is a dictionary with a name and a list of marks.
students = [
    {"name": "Aryan", "marks": [88, 92, 79]},
    {"name": "Priya", "marks": [95, 91, 97]},
    {"name": "Rahul", "marks": [60, 72, 65]},
    {"name": "Sneha", "marks": [40, 55, 48]},
]

print("=" * 40)
print("GRADE ANALYZER")
print("=" * 40)

# 1. Calculate average marks for each student using a lambda
print("\n--- Average marks ---")
for student in students:
    # sum(marks) / len(marks) gives the average
    average = (lambda marks: sum(marks) / len(marks))(student["marks"])
    print(f"{student['name']}: {average:.1f}")

# 2. Sort students by average marks (highest first) using a lambda
ranked = sorted(
    students,
    key=lambda student: sum(student["marks"]) / len(student["marks"]),
    reverse=True,
)

print("\n--- Ranking ---")
for position, student in enumerate(ranked, start=1):
    average = sum(student["marks"]) / len(student["marks"])
    print(f"{position}. {student['name']} - {average:.1f}")

# 3. Assign a grade label to each student using a lambda
assign_grade = lambda average: (
    "A" if average >= 90 else
    "B" if average >= 75 else
    "C" if average >= 60 else
    "D" if average >= 40 else
    "F"
)

print("\n--- Grades ---")
for student in ranked:
    average = sum(student["marks"]) / len(student["marks"])
    print(f"{student['name']}: Grade {assign_grade(average)}")

# 4. Find the class topper using max() with a lambda
topper = max(
    students,
    key=lambda student: sum(student["marks"]) / len(student["marks"]),
)
print(f"\nClass topper: {topper['name']}")

print("\n" + "=" * 40)
