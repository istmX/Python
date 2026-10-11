# calculator_helpers.py
# This is a CUSTOM MODULE — a file we wrote ourselves.
# Other files can import and reuse these functions.

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the quotient of two numbers.

    Raises a ValueError when dividing by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
