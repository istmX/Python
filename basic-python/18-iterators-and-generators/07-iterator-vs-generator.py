# Iterator vs Generator — and When to Use Each

# Iterator: an object with __iter__ and __next__ (custom classes).
# Generator: a function with yield that creates an iterator easily.

# Both produce items one at a time. Generators are usually simpler.

# --- Same task two ways ---

# Way 1: custom iterator class
class SquareIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current * self.current
        self.current = self.current + 1
        return value


# Way 2: generator function (much shorter)
def square_generator(limit):
    for number in range(1, limit + 1):
        yield number * number


print("Iterator:", list(SquareIterator(5)))
print("Generator:", list(square_generator(5)))

# When to use which:
# - generator function -> most cases (simple, short, readable)
# - custom iterator class -> when you need complex state or
#   extra methods alongside iteration
# - generator expression -> quick one-off generators

# All three work with for loops, next(), list(), sum(), etc.
