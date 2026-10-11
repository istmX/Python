# What Are Modules?
# A module is simply a Python file (.py) containing code you can reuse:
# functions, classes, variables.
#
# Instead of writing everything in one file, you split your code
# into modules and import what you need.

# Python comes with many built-in modules.
import math

print("Pi:", math.pi)
print("Square root of 16:", math.sqrt(16))
print("5 factorial:", math.factorial(5))

# Another built-in module
import random

print("Random number (1-10):", random.randint(1, 10))
print("Random choice:", random.choice(["red", "green", "blue"]))

# Why modules?
# - reuse code without copying it
# - keep programs organized
# - share code between projects
# - use code written by others (the standard library)
