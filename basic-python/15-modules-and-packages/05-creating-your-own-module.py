# Creating Your Own Module
# Any .py file can be a module. This file imports
# calculator_helpers.py (in the same folder) and uses it.

# Import the whole module
import calculator_helpers

print("Add:", calculator_helpers.add(10, 5))
print("Divide:", calculator_helpers.divide(10, 2))

# Or import only what you need
from calculator_helpers import multiply, subtract

print("Multiply:", multiply(6, 7))
print("Subtract:", subtract(20, 8))

# The module can also raise errors for bad input
try:
    calculator_helpers.divide(10, 0)
except ValueError as error:
    print("Error caught:", error)

# Rules for your own modules:
# - keep one module focused on one topic
# - use clear function and variable names
# - add docstrings (the triple-quoted text) to explain usage
# - keep module names lowercase with underscores if needed
