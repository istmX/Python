# Common Scope Mistakes (and How to Avoid Them)

# Mistake 1: Using a variable before assigning it locally
def broken_total():
    # total = total + 5  -> ERROR!
    # Python sees the assignment, treats 'total' as local,
    # but it has no value yet when we try to read it.
    total = 10
    total = total + 5
    print("Fixed version:", total)

broken_total()

# Mistake 2: Expecting a function to change a global by default
counter = 0

def broken_increment():
    # counter = counter + 1  -> ERROR (same reason as above)
    pass

def working_increment():
    global counter
    counter = counter + 1

working_increment()
working_increment()
print("Counter:", counter)   # 2

# Mistake 3: Shadowing — a local variable hides a global one
name = "Global Aryan"

def shadow():
    name = "Local Aryan"   # a NEW local variable, global is untouched
    print("Inside:", name)

shadow()
print("Outside:", name)     # still "Global Aryan"

# Tip: give variables clear, different names to avoid confusion.
