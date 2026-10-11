# reversed() — Iterate Backwards
# reversed() returns an iterator that goes through items in reverse.

numbers = [1, 2, 3, 4, 5]

# reversed() returns an iterator — wrap it in list() to see it
backwards = list(reversed(numbers))
print("Reversed:", backwards)
print("Original:", numbers)      # unchanged

# Loop in reverse
for number in reversed(numbers):
    print(number, end=" ")
print()

# Strings work too
print("Reversed word:", "".join(reversed("Python")))

# reversed() only works on sequences (lists, strings, tuples)
# For general iterables, convert to a list first.
# print(reversed(range(5)))  ->  actually works: range is a sequence

# Practical: checking palindromes the easy way
word = "level"
is_palindrome = list(word) == list(reversed(word))
print(f"'{word}' palindrome?", is_palindrome)
