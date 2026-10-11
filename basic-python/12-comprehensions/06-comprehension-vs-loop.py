# Comprehension vs Loop
# Both work. Choose based on readability.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Simple transformation -> comprehension is cleaner
squares_comp = [n * n for n in numbers]

squares_loop = []
for n in numbers:
    squares_loop.append(n * n)

print("Comprehension:", squares_comp)
print("Loop:         ", squares_loop)

# Complex logic -> a loop is easier to read and debug
# Example: keep numbers that are even AND whose square is below 50
result_loop = []
for n in numbers:
    if n % 2 == 0:
        square = n * n
        if square < 50:
            result_loop.append((n, square))
print("Complex loop result:", result_loop)

# The same as a comprehension (works, but harder to read):
result_comp = [(n, n * n) for n in numbers if n % 2 == 0 and n * n < 50]
print("Same with comprehension:", result_comp)

# Rule of thumb:
# - one simple operation      -> comprehension
# - multiple steps or complex ifs -> regular loop
# - comprehensions should still be easy to read at a glance
