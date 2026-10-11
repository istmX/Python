# Factorial with Recursion
# factorial(n) = n * (n-1) * (n-2) * ... * 1
# Example: 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
    # Base case: 0! and 1! both equal 1
    if n <= 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

print("5! =", factorial(5))     # 120
print("6! =", factorial(6))     # 720
print("1! =", factorial(1))     # 1
print("0! =", factorial(0))     # 1

# How factorial(4) unfolds:
#   4 * factorial(3)
#   4 * (3 * factorial(2))
#   4 * (3 * (2 * factorial(1)))
#   4 * (3 * (2 * 1))  = 24

# The same thing with a loop (for comparison):
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print("Loop version, 5! =", factorial_loop(5))   # 120
