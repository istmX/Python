# Comprehensions in Python 📦

This folder introduces **comprehensions** — a concise way to build
lists, dictionaries, and sets from existing iterables in a single line.

Comprehensions make common "loop and collect" patterns shorter
and often easier to read.

---

## 🧠 What Is a Comprehension?

A **comprehension** is a compact expression that creates a new
collection by transforming and filtering an existing one.

Loop version:

```python
squares = []
for n in range(1, 6):
    squares.append(n * n)
```

Comprehension version:

```python
squares = [n * n for n in range(1, 6)]
```

Both produce `[1, 4, 9, 16, 25]`.

---

## 🎯 Why Comprehensions Matter

Comprehensions help you:
- replace simple 3–4 line loops with one readable line
- transform and filter data in a single expression
- write more "Pythonic" code (the style Python programmers expect)

They are a tool, not a rule — use them when they improve readability.

---

## 📂 Files in This Folder

1. **`01-what-are-comprehensions.py`**
   What comprehensions are, with a loop and its comprehension
   equivalent side by side.

2. **`02-list-comprehensions.py`**
   Basic list comprehensions: transforming numbers, strings,
   and using f-strings inside the expression.

3. **`03-list-comprehension-with-condition.py`**
   Filtering with `if`, multiple conditions, and ternary
   expressions for if/else behavior.

4. **`04-dictionary-comprehensions.py`**
   Building dictionaries with `{key: value for ...}`,
   including filtering and value transformation.

5. **`05-set-comprehensions.py`**
   Building sets, automatic duplicate removal, and a common
   trick for deduplicating a list.

6. **`06-comprehension-vs-loop.py`**
   When to use a comprehension and when a regular loop
   is clearer, with a rule of thumb.

7. **`07-mini_project.py`**
   A Word Frequency Counter mini project that uses dictionary,
   set, and list comprehensions to analyze a sentence.

---

## ▶️ How to Run

Run any file using:

```bash
python filename.py
```

Example:

```bash
python 01-what-are-comprehensions.py
python 07-mini_project.py
```

---

## 🧠 Important Concepts and Syntax

```python
# List comprehension
squares = [n * n for n in range(1, 6)]

# List comprehension with a filter
evens = [n for n in range(10) if n % 2 == 0]

# Dictionary comprehension
name_lengths = {name: len(name) for name in names}

# Set comprehension
first_letters = {word[0] for word in words}
```

---

## ⚠️ Common Mistakes and Debugging Tips

1. **Using a comprehension for complex logic**
   Multiple nested `if`s and transformations become unreadable.
   Use a regular loop instead.

2. **Forgetting the brackets**
   `[...]` makes a list, `{key: value ...}` makes a dictionary,
   `{...}` makes a set. Mixing them up causes errors.

3. **Creating a set when you need order**
   Sets are unordered. If order matters, use a list.

4. **Performance trap** — calling `words.count(word)` inside a
   comprehension scans the whole list for every word (fine for
   small data, slow for big data). For large texts, use a loop
   that counts in a single pass.

---

## 🏋️ Practice Exercises

1. Create a list of the first 10 even numbers using a comprehension.
2. Given a list of words, build a dictionary mapping each word
   to `True` if it starts with a vowel, else `False`.
3. Use a set comprehension to find the unique vowels in a sentence.
4. Rewrite one of your earlier loop-based projects using
   comprehensions where appropriate.

---

## 🧩 Mini Project: Word Frequency Counter

**File:** `07-mini_project.py`

This project analyzes a sentence using comprehensions:

1. Builds a word-frequency dictionary
2. Filters for repeated words
3. Sorts words by length
4. Finds words starting with a specific letter (set comprehension)
5. Maps each word to its length

Run it and try it with your own sentence.

---

## 📚 Official Python Documentation

- List Comprehensions  
  https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

- Dictionary Comprehensions  
  https://docs.python.org/3/tutorial/datastructures.html#dictionary-comprehensions

- Set Comprehensions  
  https://docs.python.org/3/tutorial/datastructures.html#set-comprehensions

---

© 2026 ISTMX. All rights reserved.

ISTMX — Python Learning Resource  
Aryan — Developer & Maintainer
