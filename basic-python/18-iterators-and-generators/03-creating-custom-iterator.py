# Creating a Custom Iterator
# An iterator is any class that implements:
#   __iter__() -> returns the iterator object (usually self)
#   __next__() -> returns the next item (or raises StopIteration)

class Countdown:
    """Counts down from a number to 1."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        # returns the iterator object itself
        return self

    def __next__(self):
        if self.current <= 0:
            # no more items: stop the loop
            raise StopIteration
        value = self.current
        self.current = self.current - 1
        return value


# Now Countdown works with for loops and next()
countdown = Countdown(5)
for number in countdown:
    print(number, end=" ")
print()

# And manually with next()
countdown_two = Countdown(3)
print(next(countdown_two))   # 3
print(next(countdown_two))   # 2
print(next(countdown_two))   # 1

# Common mistake: forgetting to decrease the counter,
# which creates an infinite loop. Always move toward StopIteration.
