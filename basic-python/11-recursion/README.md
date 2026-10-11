# Recursion in Python 🔄

This folder introduces **recursion** — a technique where a function
calls itself to solve a smaller piece of a problem.

Recursion is a powerful way to think about problems that naturally
split into smaller copies of themselves.

---

## 🧠 What Is Recursion?

**Recursion** means a function calling **itself**.

Every recursive function has two essential parts:

1. **Base case** — the condition that stops the recursion
2. **Recursive case** — the function calls itself with a smaller input

Without a base case, the function calls itself forever
(until Python raises a `RecursionError`).

---

## 🎯 Why Recursion Matters

Recursion matters because:
- some problems are naturally recursive (trees, nested data, sequences)
- it can make code shorter and clearer for those problems
- it is a foundation for many advanced algorithms

It is **not** always the best tool — loops are often simpler and faster.

---

## 📂 Files in This Folder

1. **`01-what-is-recursion.py`**
   What recursion is, with a countdown example that shows
   the base case and recursive case.

2. **`02-base-case-and-recursive-case.py`**
   A `sum_upto(n)` function that shows exactly how recursive
   calls unfold step by step.

3. **`03-factorial-with-recursion.py`**
   The classic factorial example, with a loop version for comparison.

4. **`04-fibonacci-with-recursion.py`**
   The Fibonacci sequence, plus a warning about the performance
   cost of the simple recursive version.

5. **`05-recursion-vs-loops.py`**
   Reversing a string three ways (recursive, loop, Pythonic)
   to compare the approaches.

6. **`06-common-mistakes.py`**
   The most common recursion mistakes: missing base cases,
   never reaching the base case, and the recursion depth limit.

7. **`07-mini_project.py`**
   A Recursion Toolbox mini project with three recursive tools:
   a palindrome checker, a sum-of-digits calculator, and a
   power calculator.

---

## ▶️ How to Run

Run any file using:

```bash
python filename.py
```

Example:

```bash
python 01-what-is-recursion.py
python 07-mini_project.py
```

---

## 🧠 Important Concepts and Syntax

```python
def factorial(n):
    # Base case: stops the recursion
    if n <= 1:
        return 1
    # Recursive case: smaller problem
    return n * factorial(n - 1)
```

Rules of thumb:
- Always define the base case first
- Each recursive call must move toward the base case
- Python's default recursion limit is 1000 (`sys.getrecursionlimit()`)

---

## ⚠️ Common Mistakes and Debugging Tips

1. **RecursionError: maximum recursion depth exceeded**
   Your base case is missing or never reached. Check that each call
   makes the input smaller.

2. **Wrong result** — the base case returns the wrong value.
   Test your function with the smallest possible input first.

3. **Slow performance** — simple recursive Fibonacci recalculates
   the same values repeatedly. Use a loop for large inputs.

4. **Debugging tip** — add a `print(n)` at the start of the function
   to watch the values move toward the base case.

---

## 🏋️ Practice Exercises

1. Write a recursive function that counts how many times a letter
   appears in a string.
2. Write a recursive function that finds the largest number in a list.
3. Write a recursive function that prints numbers from 1 to n
   without using a loop.
4. Add a recursive "digital root" function to the Toolbox project
   (keep summing digits until one digit remains).

---

## 🧩 Mini Project: Recursion Toolbox

**File:** `07-mini_project.py`

This project bundles three recursive tools:

1. **Palindrome checker** — compares the first and last letters,
   then recurses on the middle of the string
2. **Sum of digits** — adds the last digit to the recursive sum
   of the remaining digits
3. **Power calculator** — multiplies the base by itself using
   `base * power(base, exponent - 1)`

Run it and try adding your own recursive function to the toolbox.

---

## 📚 Official Python Documentation

- Recursion (in the Python Tutorial's glossary)  
  https://docs.python.org/3/glossary.html#term-recursive

- `sys.getrecursionlimit()`  
  https://docs.python.org/3/library/sys.html#sys.getrecursionlimit

---

© 2026 ISTMX. All rights reserved.

ISTMX — Python Learning Resource  
Aryan — Developer & Maintainer
