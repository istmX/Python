# The yield Keyword
# yield pauses the function and hands one value to the caller.
# When next() is called again, the function RESUMES right after yield.

def greet_twice():
    print("About to yield A")
    yield "A"              # pause here, give back "A"
    print("Resumed! About to yield B")
    yield "B"              # pause here, give back "B"
    print("Resumed! Done.")

gen = greet_twice()

print(next(gen))   # prints "About to yield A", then A
print(next(gen))   # prints "Resumed! About to yield B", then B
# next(gen)        # prints "Resumed! Done." then raises StopIteration

# yield vs return:
#   return -> ends the function, hands back one final value
#   yield  -> pauses the function, resumes on the next next() call

# Because generators remember their state, they can produce
# values forever — even infinite sequences:
def infinite_counter(number=0):
    while True:            # never ends on its own
        yield number
        number = number + 1

counter = infinite_counter(10)
print(next(counter))   # 10
print(next(counter))   # 11
print(next(counter))   # 12
# ...could go forever without filling memory
