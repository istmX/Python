# What Are Exceptions?
# An exception is an error that happens while a program runs.
# If not handled, it stops the program with an error message.

# Example: this line raises a ZeroDivisionError
# result = 10 / 0

# Example: this line raises a NameError
# print(undefined_variable)

# Example: this line raises a TypeError
# total = "10" + 5

# Python has many built-in exception types.
# You will meet these often while learning:
#   ZeroDivisionError -> dividing by zero
#   NameError         -> using a variable that does not exist
#   TypeError         -> mixing incompatible types
#   ValueError        -> right type, wrong value (e.g., int("abc"))
#   FileNotFoundError -> opening a file that does not exist
#   IndexError        -> list index out of range
#   KeyError          -> dictionary key does not exist

# The good news: you can HANDLE exceptions so your program
# does not crash. That is what this folder is about.
