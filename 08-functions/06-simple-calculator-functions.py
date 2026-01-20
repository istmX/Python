# Each function does ONE specific task
# This makes code easier to read and reuse

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Taking input from the user
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Calling functions with user input
print("Addition:", add(x, y))
print("Subtraction:", subtract(x, y))
