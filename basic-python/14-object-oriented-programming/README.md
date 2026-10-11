# Object-Oriented Programming (OOP) 🧱

This folder introduces **Object-Oriented Programming** in Python —
a way of organizing code around objects that combine data (attributes)
and behavior (methods).

OOP is one of the most important topics in Python. Take your time here.

---

## 🧠 What Is OOP?

**Object-Oriented Programming** organizes code into **classes** and **objects**:

- A **class** is a blueprint (like a cookie cutter)
- An **object** is built from that blueprint (like a cookie)

Real-life example:
- Class: `Dog` (the blueprint)
- Objects: `Buddy`, `Max` (real dogs built from the blueprint)
- Attributes: name, age, breed
- Methods: bark(), eat(), sleep()

---

## 🎯 Why OOP Matters

OOP helps you:
- group related data and functions together
- reuse code through inheritance
- model real-world things naturally
- build large programs that stay organized

---

## 📂 Files in This Folder

1. **`01-introduction-to-oops.py`**
   What OOP is, with a real-life analogy and a side-by-side
   comparison of non-OOP vs OOP code.

2. **`02-classes-and-objects.py`**
   Defining a class, creating objects, and calling methods.

3. **`03-constructors-and-init.py`**
   The `__init__` constructor, the `self` parameter, and how
   objects store their own data.

4. **`04-instance-and-class-variables.py`**
   Instance variables (unique per object) vs class variables
   (shared by all objects), including the shadowing trap.

5. **`05-instance-class-and-static-methods.py`**
   The three method types: instance, class (`@classmethod`),
   and static (`@staticmethod`).

6. **`06-encapsulation.py`**
   Protecting data with public, `_protected`, and `__private`
   naming conventions, plus controlled access through methods.

7. **`07-inheritance.py`**
   Child classes reusing parent code, `isinstance()`, and
   method overriding.

8. **`08-polymorphism.py`**
   The same method name behaving differently per object,
   with a function that works on any animal.

9. **`09-abstraction.py`**
   Abstract classes with the `abc` module: defining methods
   that every child class must implement.

10. **`10-magic-methods.py`**
    Dunder methods (`__str__`, `__len__`, `__add__`, `__eq__`,
    `__lt__`) that make objects work with `print()`, `len()`,
    `+`, `==`, and `sort()`.

11. **`11-practice-exercises.py`**
    Four guided exercises: a Car class, an object counter,
    inheritance with `super()`, and encapsulation.

12. **`12-mini_project.py`**
    A Library Management System mini project combining
    abstraction, inheritance, encapsulation, and polymorphism.

---

## ▶️ How to Run

Run any file using:

```bash
python filename.py
```

Example:

```bash
python 02-classes-and-objects.py
python 12-mini_project.py
```

---

## 🧠 Important Concepts and Syntax

```python
class Dog:
    species = "Canis familiaris"      # class variable

    def __init__(self, name):         # constructor
        self.name = name              # instance variable

    def bark(self):                   # instance method
        print("Woof!")

class Puppy(Dog):                     # inheritance
    def bark(self):                   # overriding
        print("Yip!")

dog = Dog("Buddy")                    # create an object
dog.bark()                            # call a method
```

The four pillars of OOP:
- **Encapsulation** — bundle data + methods, protect data
- **Inheritance** — reuse and extend existing classes
- **Polymorphism** — same interface, different behavior
- **Abstraction** — hide complex details behind simple interfaces

---

## ⚠️ Common Mistakes and Debugging Tips

1. **Forgetting `self`**
   Instance methods must have `self` as the first parameter.
   Python passes it automatically when you call `object.method()`.

2. **Forgetting to call `self` attributes**
   Inside a class, always write `self.name`, not `name`.

3. **Name mangling confusion**
   `__balance` becomes `_ClassName__balance` internally.
   Access it through methods, not directly.

4. **Creating an abstract class object**
   Classes with `@abstractmethod` cannot be instantiated.
   Create a concrete child class instead.

5. **Forgetting `super().__init__()`**
   When overriding `__init__` in a child class, call
   `super().__init__(...)` to reuse the parent's setup.

---

## 🏋️ Practice Exercises

1. Create a `Student` class with name, marks, and a method
   that returns the grade.
2. Add a class variable that counts how many students exist.
3. Create a `Square` class that inherits from a `Shape` class
   and implements `area()` and `perimeter()`.
4. Add a `__str__` method to your class so `print(object)`
   shows something friendly.
5. Extend the Library project with a search-by-title feature.

---

## 🧩 Mini Project: Library Management System

**File:** `12-mini_project.py`

This project models a small library:

1. An abstract `LibraryItem` base class with borrow/return logic
2. Three child classes: `Book`, `Magazine`, `DVD` — each with its
   own `describe()` method (polymorphism)
3. A `Library` class that manages a catalog of items
4. A class variable that counts every item created

Run it, then try adding a search feature or a due-date system.

---

## 📚 Official Python Documentation

- Classes (Python Tutorial)  
  https://docs.python.org/3/tutorial/classes.html

- Abstract Base Classes (`abc` module)  
  https://docs.python.org/3/library/abc.html

---

© 2026 ISTMX. All rights reserved.

ISTMX — Python Learning Resource  
Aryan — Developer & Maintainer
