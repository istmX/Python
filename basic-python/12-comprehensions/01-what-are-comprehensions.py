# Comprehensions in Python
# A comprehension builds a new collection (list, dict, or set)
# from an existing one in a single readable line.

# Without a comprehension: build a list with a loop
squares_loop = []
for number in range(1, 6):
    squares_loop.append(number * number)
print("With a loop:", squares_loop)

# With a list comprehension: same result, one line
squares_comp = [number * number for number in range(1, 6)]
print("With a comprehension:", squares_comp)

# The pattern:
#   [ expression for item in collection ]
#      ^          ^         ^
#      |          |         +-- where the items come from
#      |          +-- each item, one by one
#      +-- what to store for each item

# Comprehensions are not magic — they are just a shorter way
# to write a simple loop that builds a collection.
