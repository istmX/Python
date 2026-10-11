# Base Case and Recursive Case
# These two parts make recursion work.

# Example: sum of numbers from 1 to n
def sum_upto(n):
    # Base case: sum of 1 is just 1 (nothing left to add)
    if n == 1:
        return 1

    # Recursive case: n + sum of everything below it
    return n + sum_upto(n - 1)

print("Sum from 1 to 5:", sum_upto(5))      # 15
print("Sum from 1 to 10:", sum_upto(10))    # 55

# How sum_upto(5) unfolds:
#   5 + sum_upto(4)
#   5 + (4 + sum_upto(3))
#   5 + (4 + (3 + sum_upto(2)))
#   5 + (4 + (3 + (2 + sum_upto(1))))
#   5 + (4 + (3 + (2 + 1)))  = 15

# ⚠️ If we remove the base case, the function calls itself forever
# until Python stops it with a RecursionError.
