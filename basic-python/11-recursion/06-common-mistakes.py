# Common Recursion Mistakes (and How to Avoid Them)

# Mistake 1: No base case -> infinite recursion
#
#   def broken(n):
#       return n + broken(n - 1)   # never stops!
#
# Python stops it with: RecursionError: maximum recursion depth exceeded

# Mistake 2: Recursive case that never reaches the base case
#
#   def broken_countdown(n):
#       print(n)
#       broken_countdown(n - 1)   # if n starts at -5, it goes -6, -7, ...
#
# Fix: make sure each call moves TOWARD the base case.

def safe_countdown(n):
    if n <= 0:                 # base case
        print("Done!")
        return
    print(n)
    safe_countdown(n - 1)      # moves toward 0

safe_countdown(3)

# Mistake 3: Recursion depth limit
# Python limits recursion depth (usually 1000) to protect your program.
import sys
print("Recursion limit:", sys.getrecursionlimit())

# For very deep problems, use a loop instead, or increase the limit:
# sys.setrecursionlimit(2000)   # possible, but use with care

# Mistake 4: Repeating the same work
# The simple fibonacci(n) recalculates the same values many times.
# For learning it is fine; for real programs, prefer loops or caching.
