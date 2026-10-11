# Catching Specific Exceptions
# Catch the exact error you expect — not everything.

# BAD practice: catching everything hides real bugs
try:
    result = 10 / 0
except:                    # catches ALL exceptions (too broad!)
    print("Something went wrong.")

# GOOD practice: catch the specific exception you expect
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")

# You can have multiple except blocks for different errors
def divide_values(a, b):
    try:
        result = int(a) / int(b)
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")
    except ValueError:
        print("Error: both inputs must be numbers.")

divide_values("10", "2")    # Result: 5.0
divide_values("10", "0")    # Error: cannot divide by zero.
divide_values("abc", "2")   # Error: both inputs must be numbers.

# You can also catch several types in one block:
try:
    data = {"name": "Aryan"}
    print(data["age"])        # KeyError
except (KeyError, IndexError) as error:
    print("Lookup failed:", error)

# The 'as error' part lets you see the actual error message.
