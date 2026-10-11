# Python Scope: Where Variables Live
# Scope decides where a variable can be seen and used.

# Python has these scopes (from innermost to outermost):
#   Local      -> inside the current function
#   Enclosing  -> inside any enclosing (outer) function
#   Global     -> at the top level of the file
#   Built-in   -> names Python provides (print, len, etc.)

# A simple rule to remember (the LEGB rule):
# Python looks for a name in this order:
#   Local -> Enclosing -> Global -> Built-in

# Example: a local variable
def show_local():
    message = "I am local"   # created inside the function
    print(message)           # visible here

show_local()

# print(message)  # ERROR: message does not exist outside the function

# Example: a global variable
app_name = "ISTMX Python"    # created at the top level

def show_global():
    print(app_name)          # global variables are readable inside functions

show_global()
print(app_name)              # and outside too
