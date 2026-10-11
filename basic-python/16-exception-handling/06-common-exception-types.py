# Common Exception Types You Will Meet

# ZeroDivisionError -> division by zero
try:
    10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

# ValueError -> right type, wrong value
try:
    int("abc")
except ValueError as e:
    print("ValueError:", e)

# TypeError -> incompatible types
try:
    "10" + 5
except TypeError as e:
    print("TypeError:", e)

# NameError -> variable not defined
try:
    print(unknown_variable)
except NameError as e:
    print("NameError:", e)

# KeyError -> missing dictionary key
try:
    data = {"name": "Aryan"}
    print(data["age"])
except KeyError as e:
    print("KeyError:", e)

# IndexError -> list index out of range
try:
    items = [1, 2, 3]
    print(items[10])
except IndexError as e:
    print("IndexError:", e)

# FileNotFoundError -> file does not exist
try:
    open("no_such_file.txt")
except FileNotFoundError as e:
    print("FileNotFoundError:", e)

# Tip: the error message after the colon tells you WHAT went wrong.
# Always read it carefully while debugging.
