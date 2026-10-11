# Functional Programming Tools: map, filter, reduce
# These functions process collections by applying a function
# to each item — without writing an explicit loop.

# The three tools:
#   map()    -> transform every item
#   filter() -> keep only items that match a condition
#   reduce() -> combine all items into a single value

# map() and filter() are built-in.
# reduce() lives in the functools module (must be imported).

from functools import reduce

# A simple list to work with
numbers = [1, 2, 3, 4, 5]

# map: double every item
doubled = list(map(lambda n: n * 2, numbers))
print("Doubled:", doubled)

# filter: keep only even numbers
evens = list(filter(lambda n: n % 2 == 0, numbers))
print("Evens:", evens)

# reduce: add all items together
total = reduce(lambda a, b: a + b, numbers)
print("Total:", total)

# Why "functional"?
# Instead of telling Python HOW to loop (for/while),
# you tell it WHAT to do with each item (a function).
