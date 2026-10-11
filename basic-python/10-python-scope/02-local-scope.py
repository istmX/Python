# Local Scope
# A variable created inside a function belongs to that function only.
# It is created when the function is called and destroyed when it ends.

def my_function():
    score = 100        # local variable
    print("Inside the function:", score)

my_function()

# print(score)  # ERROR: score is not defined outside the function

# Two functions can use the same variable name without clashing.
# Each function gets its own separate copy.

def function_a():
    value = "A"
    print(value)

def function_b():
    value = "B"
    print(value)

function_a()  # A
function_b()  # B

# Parameters are also local variables
def greet(name):      # 'name' exists only inside greet
    print("Hello", name)

greet("Aryan")
# print(name)  # ERROR: name is local to greet()
