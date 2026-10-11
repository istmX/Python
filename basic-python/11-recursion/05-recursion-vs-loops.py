# Recursion vs Loops
# Anything recursion can do, a loop can also do (and vice versa).
# The difference is style, readability, and sometimes performance.

# Task: reverse a string

# Recursive version
def reverse_recursive(text):
    # Base case: an empty string is its own reverse
    if len(text) == 0:
        return ""
    # Recursive case: last letter + reverse of the rest
    return text[-1] + reverse_recursive(text[:-1])

# Loop version
def reverse_loop(text):
    result = ""
    for letter in text:
        result = letter + result   # put each new letter in front
    return result

# Pythonic version (the one real programmers use)
def reverse_pythonic(text):
    return text[::-1]

word = "Python"
print("Recursive:", reverse_recursive(word))
print("Loop:     ", reverse_loop(word))
print("Pythonic: ", reverse_pythonic(word))

# When to prefer recursion:
# - problems that naturally split into smaller copies of themselves
#   (trees, nested data, divide-and-conquer algorithms)
#
# When to prefer loops:
# - simple repetition
# - performance (recursion uses more memory)
# - deep recursion can hit Python's recursion limit
