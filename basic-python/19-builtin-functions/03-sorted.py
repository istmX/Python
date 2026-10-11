# sorted() — Sort Any Iterable
# sorted() returns a NEW sorted list and leaves the original unchanged.

numbers = [5, 2, 9, 1, 7]
print("Original:", numbers)

ascending = sorted(numbers)
print("Ascending:", ascending)
print("Original still:", numbers)     # unchanged!

descending = sorted(numbers, reverse=True)
print("Descending:", descending)

# Sort strings alphabetically
names = ["Rahul", "Aryan", "Priya"]
print("Sorted names:", sorted(names))

# Sort by a custom key (e.g., by length)
words = ["elephant", "cat", "giraffe"]
by_length = sorted(words, key=len)
print("By length:", by_length)

# Sort a dictionary by value
marks = {"Aryan": 88, "Priya": 95, "Rahul": 72}
top_scorers = sorted(marks, key=marks.get, reverse=True)
print("Students by marks:", top_scorers)

# Note: lists also have a .sort() method, but it sorts IN PLACE
# and returns None. Use sorted() when you want a new list.
