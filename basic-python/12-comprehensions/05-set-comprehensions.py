# Set Comprehensions
# Build sets (unique, unordered values) in one line with { ... }

# Squares of numbers — duplicates are removed automatically
squares = {n * n for n in range(1, 8)}
print("Squares set:", squares)

# Unique first letters of words
words = ["apple", "apricot", "banana", "cherry", "blueberry"]
first_letters = {word[0] for word in words}
print("First letters:", first_letters)

# With a condition: unique word lengths for long words only
sentence = "Python is a friendly language for beginners"
unique_lengths = {len(word) for word in sentence.split() if len(word) > 4}
print("Unique lengths of long words:", unique_lengths)

# Sets vs lists:
#   { ... } -> set:  unordered, no duplicates
#   [ ... ] -> list: ordered, allows duplicates

# Common use: remove duplicates from a list
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = list({n for n in numbers})
print("Unique numbers:", unique_numbers)
