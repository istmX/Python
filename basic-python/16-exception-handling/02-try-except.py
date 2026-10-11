# try and except
# Wrap risky code in try. If an exception happens,
# Python jumps to the except block instead of crashing.

# Basic example: dividing two numbers
numerator = 10
denominator = 0

try:
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("You cannot divide by zero!")

print("The program continues running.")

# Another example: converting user input to an integer
user_input = "abc"

try:
    number = int(user_input)
    print("You entered:", number)
except ValueError:
    print(f"'{user_input}' is not a valid integer.")

print("Still running!")

# The pattern:
#   try:
#       risky code
# except SomeException:
#       what to do when it fails
