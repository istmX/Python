# Fibonacci Sequence with Recursion
# Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Each number is the sum of the two before it.

def fibonacci(n):
    # Base cases: the first two numbers are fixed
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case: sum of the two previous numbers
    return fibonacci(n - 1) + fibonacci(n - 2)

# Print the first 10 Fibonacci numbers
print("First 10 Fibonacci numbers:")
for i in range(10):
    print(fibonacci(i), end=" ")
print()

# ⚠️ Warning: this simple version is slow for large n.
# fibonacci(35) calls fibonacci many times over and over.
# For big inputs, loops or "memoization" are better (later topics).

# Loop version (much faster for large n):
def fibonacci_loop(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print("Loop version, 40th number:", fibonacci_loop(40))   # 102334155
