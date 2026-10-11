# Generator Expressions
# A compact way to create generators — like list comprehensions
# but with parentheses instead of brackets.

# List comprehension: builds the whole list in memory
squares_list = [n * n for n in range(1, 6)]
print("List:", squares_list)

# Generator expression: produces items one at a time
squares_gen = (n * n for n in range(1, 6))
print("Generator:", squares_gen)

# Pull items with next()
print(next(squares_gen))   # 1
print(next(squares_gen))   # 4
print(next(squares_gen))   # 9

# Or loop over the rest
for value in squares_gen:
    print(value, end=" ")   # 16 25
print()

# Generator expressions shine inside functions that consume iterables:
total = sum(n * n for n in range(1, 6))       # no extra brackets needed
print("Sum of squares:", total)               # 55

largest = max(len(word) for word in ["cat", "elephant", "dog"])
print("Longest word length:", largest)         # 8

# Rule of thumb:
# [ ... ] -> list (fast access, more memory)
# ( ... ) -> generator (one-by-one, almost no memory)
