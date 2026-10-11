# The map() Function
# map(function, iterable) applies the function to every item
# and returns a map object (convert it with list() to see it).

# Example 1: convert strings to integers
texts = ["10", "20", "30"]
numbers = list(map(int, texts))
print("As integers:", numbers)

# Example 2: square each number
squares = list(map(lambda n: n * n, numbers))
print("Squares:", squares)

# Example 3: with a named function instead of a lambda
def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

temperatures_f = [32, 68, 100, 212]
temperatures_c = list(map(to_celsius, temperatures_f))
print("Celsius:", [round(t, 1) for t in temperatures_c])

# map() can take MULTIPLE iterables.
# The function must accept one argument from each iterable.
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print("Pairwise sums:", sums)

# map() stops when the shortest iterable is exhausted.
c = [100, 200]
short_sums = list(map(lambda x, y: x + y, a, c))
print("Shortest wins:", short_sums)
