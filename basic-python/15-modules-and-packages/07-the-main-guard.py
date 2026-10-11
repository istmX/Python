# The if __name__ == "__main__": Guard
# When you import a module, Python runs ALL its top-level code.
# The main guard prevents that code from running on import.

# This file demonstrates the guard. Try importing it from another
# file: the demo code below will NOT run automatically.

def greet(name):
    return f"Hello, {name}!"


def add(a, b):
    return a + b


# Code inside this block runs ONLY when the file is executed directly
# (python 07-the-main-guard.py), NOT when it is imported.
if __name__ == "__main__":
    print("This file was run directly.")
    print(greet("Aryan"))
    print("2 + 3 =", add(2, 3))

# Why this matters:
# - modules should define functions/classes without side effects
# - test or demo code belongs inside the guard
# - it lets a file be BOTH a module AND a runnable script
