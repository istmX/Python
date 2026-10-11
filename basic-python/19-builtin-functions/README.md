# Useful Built-in Functions 🧰

This folder introduces the most useful **built-in functions** in Python
— the tools you will use in almost every program.

Python provides these functions ready to use. No imports needed.

---

## 🧠 What Are Built-in Functions?

**Built-in functions** are functions Python gives you for free:
`print()`, `len()`, `sum()`, `sorted()`, `enumerate()`, `zip()`,
`any()`, `all()`, type converters, and many more.

---

## 🎯 Why They Matter

They help you:
- write less code (no loops for common tasks)
- process collections quickly and safely
- convert between data types
- write clean, professional, Pythonic code

---

## 📂 Files in This Folder

1. **`01-enumerate.py`**
   Looping with index + item using `enumerate()`.

2. **`02-zip.py`**
   Pairing multiple lists with `zip()`, building dictionaries,
   and unzipping with `zip(*...)`.

3. **`03-sorted.py`**
   Sorting with `sorted()`, `reverse=True`, custom `key` functions,
   and the difference from `.sort()`.

4. **`04-reversed.py`**
   Iterating backwards with `reversed()` and a palindrome trick.

5. **`05-len-sum-min-max-abs-round.py`**
   The numeric essentials: `len()`, `sum()`, `min()`, `max()`,
   `abs()`, and `round()`.

6. **`06-any-all.py`**
   Checking conditions across items with `any()` and `all()`.

7. **`07-type-conversion-builtins.py`**
   `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`,
   `set()`, and `dict()` conversions.

8. **`08-mini_project.py`**
   A Grade Statistics Analyzer mini project that combines
   `sum()`, `len()`, `min()`, `max()`, `sorted()`, `enumerate()`,
   `any()`, and `all()`.

---

## ▶️ How to Run

Run any file using:

```bash
python filename.py
```

Example:

```bash
python 01-enumerate.py
python 08-mini_project.py
```

---

## 🧠 Important Concepts and Syntax

```python
enumerate(items, start=0)   # index + item
zip(a, b)                   # pair items
sorted(items, key=fn, reverse=True)
reversed(items)             # backwards iterator
len, sum, min, max, abs, round
any(condition for x in items)
all(condition for x in items)
int(), float(), str(), bool(), list(), tuple(), set(), dict()
```

---

## ⚠️ Common Mistakes and Debugging Tips

1. **`.sort()` vs `sorted()`**
   `.sort()` sorts a list in place and returns `None`.
   `sorted()` returns a new list and keeps the original.

2. **`round(2.5)` gives `2`**
   Python uses banker's rounding (rounds to the nearest even number).
   Don't use `round()` for money — use the `decimal` module.

3. **`zip()` stops at the shortest list**
   Extra items in longer lists are silently ignored.

4. **`reversed()` returns an iterator**
   Wrap it in `list()` if you need a list.

5. **`all([])` is `True` but `any([])` is `False`**
   Remember this when validating empty collections.

---

## 🏋️ Practice Exercises

1. Use `enumerate()` to print a numbered shopping list.
2. Use `zip()` to combine subject names with marks and print a report.
3. Use `sorted()` with a `key` to sort words by their last letter.
4. Use `any()` / `all()` to validate a list of passwords (all at
   least 8 characters).
5. Use `min()` with a `key` to find the shortest word in a sentence.

---

## 🧩 Mini Project: Grade Statistics Analyzer

**File:** `08-mini_project.py`

This project computes class statistics using built-ins:

1. Averages with `sum()` and `len()`
2. Class average, highest, and lowest with `min()` / `max()`
3. Topper with `max(key=...)`
4. Ranking with `sorted()` and `enumerate()`
5. Pass/fail counts with `sum()` and a condition
6. Whole-class checks with `all()` and `any()`

Run it and try adding more students or subjects.

---

## 📚 Official Python Documentation

- Built-in Functions (complete reference)  
  https://docs.python.org/3/library/functions.html

---

© 2026 ISTMX. All rights reserved.

ISTMX — Python Learning Resource  
Aryan — Developer & Maintainer
