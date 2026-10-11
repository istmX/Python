# Mini Project: Library Management System
# This project uses OOP to manage a small library.
# It combines classes, inheritance, encapsulation, and polymorphism.

from abc import ABC, abstractmethod


# ---------- Base class ----------
class LibraryItem(ABC):
    """Abstract base class for all items in the library."""

    total_items = 0   # class variable: counts every item created

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_borrowed = False
        LibraryItem.total_items = LibraryItem.total_items + 1

    def borrow(self):
        if self.is_borrowed:
            print(f"'{self.title}' is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"You borrowed '{self.title}'.")

    def return_item(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")

    @abstractmethod
    def describe(self):
        """Every item must describe itself differently."""
        pass

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"[{self.item_id}] {self.title} - {status}"


# ---------- Child classes ----------
class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def describe(self):
        print(f"Book: '{self.title}' by {self.author}, {self.pages} pages")


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue):
        super().__init__(title, item_id)
        self.issue = issue

    def describe(self):
        print(f"Magazine: '{self.title}', Issue #{self.issue}")


class DVD(LibraryItem):
    def __init__(self, title, item_id, duration):
        super().__init__(title, item_id)
        self.duration = duration

    def describe(self):
        print(f"DVD: '{self.title}', {self.duration} minutes")


# ---------- Library ----------
class Library:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added '{item.title}' to the library.")

    def show_catalog(self):
        print(f"\n--- {self.name} Catalog ---")
        for item in self.items:
            print(item)

    def show_descriptions(self):
        # Polymorphism: each item describes itself its own way
        print("\n--- Item Descriptions ---")
        for item in self.items:
            item.describe()


# ---------- Run the library ----------
library = Library("ISTMX Library")

book = Book("Python Basics", "B001", "Aryan", 250)
magazine = Magazine("Tech Today", "M001", 42)
dvd = DVD("Learn Python", "D001", 120)

library.add_item(book)
library.add_item(magazine)
library.add_item(dvd)

library.show_catalog()
library.show_descriptions()

# Borrow and return
print()
book.borrow()          # You borrowed 'Python Basics'.
book.borrow()          # 'Python Basics' is already borrowed.
magazine.borrow()      # You borrowed 'Tech Today'.
book.return_item()     # You returned 'Python Basics'.

library.show_catalog()
print("Total items in library:", LibraryItem.total_items)
