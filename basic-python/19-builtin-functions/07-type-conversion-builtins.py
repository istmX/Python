# Type Conversion Built-ins
# Python provides built-in functions to convert between types.

# int() — convert to integer
print(int("42"))          # 42
print(int(3.99))          # 3  (truncates, does not round)
print(int("101", 2))      # 5  (binary string to integer!)

# float() — convert to decimal number
print(float("3.14"))      # 3.14
print(float(7))           # 7.0

# str() — convert to string
print(str(42))            # "42"
print(str(3.14))          # "3.14"
print(str(True))          # "True"

# bool() — convert to boolean
print(bool(1))            # True
print(bool(0))            # False
print(bool("hello"))      # True
print(bool(""))           # False (empty string is falsy)
print(bool([]))           # False (empty list is falsy)

# list() — convert to list
print(list("abc"))        # ['a', 'b', 'c']
print(list((1, 2, 3)))    # [1, 2, 3] (tuple to list)

# tuple() — convert to tuple
print(tuple([1, 2, 3]))   # (1, 2, 3)

# set() — convert to set (removes duplicates)
print(set([1, 2, 2, 3]))  # {1, 2, 3}

# dict() — build a dictionary from pairs
print(dict([("a", 1), ("b", 2)]))   # {'a': 1, 'b': 2}

# These conversions are everywhere in real code —
# especially int()/float() on user input and str() for output.
