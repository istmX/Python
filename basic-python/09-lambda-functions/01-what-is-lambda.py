# Lambda Functions in Python
# A lambda function is a small anonymous (nameless) function.

# Normal function
def square(num):
    return num * num

print("Normal function:", square(5))

# The same function written as a lambda
square_lambda = lambda num: num * num

print("Lambda function:", square_lambda(5))

# Breaking it down:
# lambda num: num * num
#   ^        ^
#   |        |
#   |        +-- what the function returns
#   +-- the input (parameter)

# A lambda can have only ONE expression.
# It cannot contain multiple lines or statements like a normal function.

# Lambdas are often used when you need a simple function
# for a short time, without naming it.
