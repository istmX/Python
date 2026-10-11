# What Are Generators?
# A generator is a special function that produces items ONE AT A TIME
# instead of computing them all at once.
#
# Instead of return, it uses yield.

def countdown_generator(start):
    while start > 0:
        yield start        # "return" one item, but REMEMBER where we stopped
        start = start - 1


# Calling a generator function does NOT run the body —
# it returns a generator object.
generator = countdown_generator(5)
print("Generator object:", generator)

# Items are produced lazily, one at a time, with next()
print(next(generator))   # 5
print(next(generator))   # 4
print(next(generator))   # 3
# ...continues until 1, then raises StopIteration

# Generators work beautifully with for loops
for number in countdown_generator(5):
    print(number, end=" ")
print()

# The big win: memory efficiency.
# A list of 1,000,000 numbers holds everything in memory.
# A generator produces them one by one — almost no memory used.
