# Mini Project: Grade Statistics Analyzer
# This project uses Python's built-in functions to compute
# statistics for a class of students.

students = [
    {"name": "Aryan", "marks": [88, 92, 79]},
    {"name": "Priya", "marks": [95, 91, 97]},
    {"name": "Rahul", "marks": [60, 72, 65]},
    {"name": "Sneha", "marks": [40, 55, 48]},
    {"name": "Vikram", "marks": [78, 81, 74]},
]

print("=" * 45)
print("GRADE STATISTICS ANALYZER")
print("=" * 45)

# 1. Calculate each student's average using sum() and len()
averages = {}
for student in students:
    average = sum(student["marks"]) / len(student["marks"])
    averages[student["name"]] = round(average, 1)

print("\n--- Averages ---")
for name, average in averages.items():
    print(f"{name}: {average}")

# 2. Class statistics using min(), max(), and sum()
all_averages = list(averages.values())
class_average = sum(all_averages) / len(all_averages)
print(f"\nClass average: {round(class_average, 1)}")
print(f"Highest average: {max(all_averages)}")
print(f"Lowest average: {min(all_averages)}")

# 3. Topper using max() with a key
topper = max(averages, key=averages.get)
print(f"Topper: {topper} ({averages[topper]})")

# 4. Students sorted by average (descending) using sorted()
ranking = sorted(averages, key=averages.get, reverse=True)
print("\n--- Ranking ---")
for position, name in enumerate(ranking, start=1):
    print(f"{position}. {name} - {averages[name]}")

# 5. Pass/fail count using any() and sum()
pass_count = sum(1 for avg in all_averages if avg >= 40)
fail_count = len(all_averages) - pass_count
print(f"\nPassed: {pass_count}, Failed: {fail_count}")

# 6. Check if the whole class passed with any()
all_passed = all(avg >= 40 for avg in all_averages)
print("Whole class passed?", "Yes" if all_passed else "No")

# 7. Any perfect scores? (100 in any subject)
perfect = any(
    100 in student["marks"]
    for student in students
)
print("Any perfect 100 score?", "Yes" if perfect else "No")

print("\n" + "=" * 45)
