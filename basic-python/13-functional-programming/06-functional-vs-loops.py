# Functional Tools vs Loops
# Same results — different style. Learn to choose.

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Task: sum of squares of even numbers

# Style 1: loop (clear step-by-step logic)
total_loop = 0
for n in numbers:
    if n % 2 == 0:
        total_loop = total_loop + n * n
print("Loop style:", total_loop)

# Style 2: comprehension (compact and Pythonic)
total_comp = sum(n * n for n in numbers if n % 2 == 0)
print("Comprehension style:", total_comp)

# Style 3: functional pipeline
total_functional = reduce(
    lambda a, b: a + b,
    map(lambda n: n * n, filter(lambda n: n % 2 == 0, numbers)),
    0,
)
print("Functional style:", total_functional)

# All three give the same answer: 220

# How to choose:
# - loop        -> best when logic has many steps or side effects
# - comprehension -> best for simple transform + filter (very Pythonic)
# - map/filter/reduce -> best when each step is a simple function
#   and you want to chain them as a pipeline

# Readability counts most: pick the style a beginner can understand.
