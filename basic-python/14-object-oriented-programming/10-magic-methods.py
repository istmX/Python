# Magic Methods (Dunder Methods)
# Magic methods are special methods with double underscores.
# They let your objects work with Python's built-in features
# like printing, adding, and comparing.

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    # __str__ controls what print() shows
    def __str__(self):
        return f"'{self.title}' ({self.pages} pages)"

    # __len__ lets the object work with len()
    def __len__(self):
        return self.pages

    # __add__ lets you use + between two objects
    def __add__(self, other):
        return Book(self.title + " & " + other.title, self.pages + other.pages)

    # __eq__ lets you compare objects with ==
    def __eq__(self, other):
        return self.title == other.title and self.pages == other.pages

    # __lt__ (less than) lets you sort objects
    def __lt__(self, other):
        return self.pages < other.pages


book_one = Book("Python Basics", 200)
book_two = Book("OOP in Python", 300)

# Without __str__, print would show a memory address.
print(book_one)                 # 'Python Basics' (200 pages)

# len() works because of __len__
print("Pages:", len(book_one))  # 200

# + works because of __add__
combined = book_one + book_two
print(combined)                 # 'Python Basics & OOP in Python' (500 pages)

# == works because of __eq__
print(book_one == Book("Python Basics", 200))   # True
print(book_one == book_two)                     # False

# Sorting works because of __lt__
shelf = [book_two, book_one, Book("Short Story", 50)]
shelf.sort()
for book in shelf:
    print(book)

# Common magic methods:
# __init__  -> constructor (runs on creation)
# __str__   -> readable text for print()
# __repr__  -> official text representation
# __len__   -> behavior of len()
# __add__   -> behavior of +
# __eq__    -> behavior of ==
