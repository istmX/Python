# The filter() Function
# filter(function, iterable) keeps only the items for which
# the function returns True.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
evens = list(filter(lambda n: n % 2 == 0, numbers))
print("Evens:", evens)

# Keep only numbers greater than 5
big = list(filter(lambda n: n > 5, numbers))
print("Greater than 5:", big)

# The function can also return any "truthy" value.
# Items with truthy results are kept; falsy ones are dropped.
values = [0, 1, "", "hello", [], [1, 2], None, True]
truthy = list(filter(None, values))   # None means "use the item itself"
print("Truthy values:", truthy)

# filter() with a named function
def is_long_word(word):
    return len(word) > 4

words = ["cat", "elephant", "dog", "giraffe", "ant"]
long_words = list(filter(is_long_word, words))
print("Long words:", long_words)

# Note: filter() only SELECTS items — it never changes them.
# To change items, use map(). To do both, combine them.
