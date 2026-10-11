# What Are Iterators?
# An iterator is an object that lets you go through items one by one.
# You have been using iterators all along: for loops use them!

# for loops work on "iterables" (lists, strings, ranges, ...)
# An iterable can produce an iterator with iter()

numbers = [10, 20, 30]

# Behind the scenes, the for loop does this:
iterator = iter(numbers)     # get an iterator from the iterable

print(next(iterator))        # 10
print(next(iterator))        # 20
print(next(iterator))        # 30
# next(iterator)             # would raise StopIteration (no more items)

# Strings are iterable too
letter_iterator = iter("Hi")
print(next(letter_iterator))   # H
print(next(letter_iterator))   # i

# Why care about iterators?
# - they produce items ONE AT A TIME (memory efficient)
# - they can represent infinite sequences
# - they are the foundation of generators (next file)
