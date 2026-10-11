# List Comprehensions
# The most common comprehension type.

# Basic: transform each item
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print("Doubled:", doubled)

# Works with strings too
names = ["aryan", "priya", "rahul"]
upper_names = [name.upper() for name in names]
print("Uppercase names:", upper_names)

# Works with any iterable (range, string, etc.)
lengths = [len(word) for word in "Python is fun".split()]
print("Word lengths:", lengths)

# You can use expressions, not just simple operations
labels = [f"Item {n}" for n in range(1, 4)]
print("Labels:", labels)

# Equivalent loop version of the first example:
doubled_loop = []
for n in numbers:
    doubled_loop.append(n * 2)
print("Loop version:", doubled_loop)
