# iter() and next() in Detail
# next() fetches the next item.
# When items run out, next() raises StopIteration.

colors = ["red", "green", "blue"]
color_iterator = iter(colors)

# Fetch items one by one
first = next(color_iterator)
second = next(color_iterator)
third = next(color_iterator)
print(first, second, third)

# This raises StopIteration:
# next(color_iterator)

# next() can take a default value instead of raising an error:
empty_iterator = iter([])
result = next(empty_iterator, "no more items")
print("With default:", result)

# Behind the scenes of a for loop:
# it calls iter(), then next() repeatedly, and stops at StopIteration.
# That means you can write your own objects that work with for loops —
# as long as they implement the iterator protocol (see the next file).
