# Recursion in Python
# Recursion means a function calling ITSELF to solve a smaller piece
# of the problem, until the problem becomes trivial.

# Classic example: countdown
def countdown(number):
    if number <= 0:                 # base case: stop condition
        print("Liftoff!")
        return
    print(number)
    countdown(number - 1)           # recursive call: smaller problem

countdown(5)

# Output:
# 5
# 4
# 3
# 2
# 1
# Liftoff!

# Every recursive function needs TWO parts:
# 1. Base case  -> when to stop (without it, the function runs forever)
# 2. Recursive case -> the function calls itself with a smaller input
