# enumerate() — Loop with Index
# Normally a for loop gives you only the item.
# enumerate() gives you the INDEX and the item together.

fruits = ["apple", "banana", "cherry"]

# Without enumerate: no index
for fruit in fruits:
    print(fruit)

print("---")

# With enumerate: index + item
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Output:
# 0: apple
# 1: banana
# 2: cherry

# Start counting from a different number
for position, fruit in enumerate(fruits, start=1):
    print(f"{position}. {fruit}")

# Very useful for numbered menus and reports
print("\nFruit list:")
for number, fruit in enumerate(fruits, start=1):
    print(f"{number}) {fruit.capitalize()}")
