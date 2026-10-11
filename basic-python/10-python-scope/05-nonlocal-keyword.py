# The nonlocal Keyword
# nonlocal is used inside a nested (inner) function
# when you want to change a variable from the enclosing (outer) function.

def outer():
    count = 0                    # belongs to outer()

    def inner():
        nonlocal count           # use outer()'s count, not a new local one
        count = count + 1
        print("Inner count:", count)

    inner()
    inner()
    print("Outer count:", count)  # outer's count was changed

outer()

# nonlocal vs global:
#   global   -> refers to a variable at the top level of the file
#   nonlocal -> refers to a variable in the nearest enclosing function

# nonlocal only works when there IS an enclosing function variable.
# If the name exists only globally, use global instead.
