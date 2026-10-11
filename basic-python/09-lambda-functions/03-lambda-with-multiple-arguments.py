# Lambda Functions with Multiple Arguments

# A lambda can take as many arguments as you want.
add = lambda a, b: a + b
print("Two arguments:", add(5, 3))

greet = lambda first, last: f"Hello, {first} {last}!"
print("Greeting:", greet("Aryan", "Sharma"))

# Default values work too
power = lambda base, exponent=2: base ** exponent
print("Square (default exponent):", power(4))
print("Cube:", power(4, 3))

# Remember:
# - separate arguments with commas
# - separate each argument and its default value with =
# - the expression after the colon is what gets returned
