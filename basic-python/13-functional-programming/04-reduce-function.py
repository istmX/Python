# The reduce() Function
# reduce(function, iterable) combines all items into ONE value
# by repeatedly applying the function to pairs.
#
# reduce must be imported from functools.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Add all numbers: ((((1+2)+3)+4)+5) = 15
total = reduce(lambda a, b: a + b, numbers)
print("Sum:", total)

# Multiply all numbers: 1*2*3*4*5 = 120
product = reduce(lambda a, b: a * b, numbers)
print("Product:", product)

# Find the largest number
largest = reduce(lambda a, b: a if a > b else b, numbers)
print("Largest:", largest)

# reduce() with an initial value
# The starting value is placed before all items.
total_with_start = reduce(lambda a, b: a + b, numbers, 100)
print("Sum starting from 100:", total_with_start)   # 115

# A realistic example: join words into a sentence
words = ["Python", "is", "fun"]
sentence = reduce(lambda a, b: a + " " + b, words)
print("Sentence:", sentence)

# ⚠️ When the list is empty and no initial value is given,
# reduce() raises a TypeError. Always consider an initial value
# for safety, or handle empty lists separately.
