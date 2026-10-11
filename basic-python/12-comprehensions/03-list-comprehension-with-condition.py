# List Comprehensions with a Condition
# Add 'if' at the end to keep only the items you want.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
evens = [n for n in numbers if n % 2 == 0]
print("Evens:", evens)

# Transform AND filter: square only the numbers greater than 4
big_squares = [n * n for n in numbers if n > 4]
print("Squares above 4:", big_squares)

# The pattern:
#   [ expression for item in collection if condition ]

# Multiple conditions work too
result = [n for n in numbers if n % 2 == 0 and n > 5]
print("Evens greater than 5:", result)

# Equivalent loop version:
evens_loop = []
for n in numbers:
    if n % 2 == 0:
        evens_loop.append(n)
print("Loop version:", evens_loop)

# Tip: if you need an 'else', the condition moves into the expression
# (ternary style) — see the next example.
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print("Labels:", labels)
