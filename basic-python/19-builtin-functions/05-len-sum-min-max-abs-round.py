# Handy Numeric and Sequence Built-ins

numbers = [4, 8, 15, 16, 23, 42]

# len() — how many items?
print("Count:", len(numbers))

# sum() — total of all items
print("Sum:", sum(numbers))

# min() and max() — smallest and largest
print("Min:", min(numbers))
print("Max:", max(numbers))

# min/max work on strings too (alphabetical order)
words = ["zebra", "apple", "mango"]
print("First alphabetically:", min(words))
print("Last alphabetically:", max(words))

# abs() — absolute value (distance from zero)
print("Absolute of -7:", abs(-7))
print("Absolute of 3.5:", abs(-3.5))

# round() — round to nearest integer or decimals
print("Round 3.14159:", round(3.14159))
print("Round to 2 decimals:", round(3.14159, 2))
print("Round 2.5:", round(2.5))     # 2 (banker's rounding!)
print("Round 3.5:", round(3.5))     # 4

# sum() with a starting value
print("Sum starting at 100:", sum(numbers, 100))

# min/max with a key function
students = [("Aryan", 88), ("Priya", 95), ("Rahul", 72)]
topper = max(students, key=lambda student: student[1])
print("Topper:", topper)
