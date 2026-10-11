# Lambda Functions in Python ⚡

This folder introduces **lambda functions** in Python.

A lambda function is a small, anonymous (nameless) function that is
defined in a single line. It is useful when you need a simple function
for a short time — especially when passing it to another function
like `sorted()` or `max()`.

---

## 🧠 What Is a Lambda Function?

A **lambda function** is a function without a name.

Normal function:

```python
def square(num):
    return num * num
```

The same thing as a lambda:

```python
square = lambda num: num * num
```

Key rules:
- A lambda can take any number of arguments
- A lambda can contain only **one expression**
- The result of that expression is returned automatically
- A lambda cannot contain multiple statements or complex logic

---

## 🎯 Why Lambdas Matter

Lambdas help you:
- write short functions quickly
- pass small pieces of logic directly to other functions
- keep code compact when the function is used only once

They are **not** a replacement for normal functions.
Use them for simple one-line logic only.

---

## 📂 Files in This Folder

1. **`01-what-is-lambda.py`**
   What a lambda is and its basic syntax (`lambda num: num * num`).
   Shows a normal function and its lambda equivalent side by side.

2. **`02-lambda-vs-regular-function.py`**
   Compares lambda and regular functions, explains when to use each,
   and shows a common mistake (overusing lambdas for reusable code).

3. **`03-lambda-with-multiple-arguments.py`**
   Lambdas with two or more arguments, and default argument values.

4. **`04-lambda-conditional-logic.py`**
   Using `if / else` inside a lambda with ternary expressions,
   plus a note on when lambdas become too complex to read.

5. **`05-lambda-with-sorted-and-max.py`**
   The most common real use of lambdas: passing them to `sorted()`,
   `max()`, and `min()` as the `key` function.

6. **`06-mini_project.py`**
   A Grade Analyzer mini project that uses lambdas to calculate averages,
   rank students, assign grades, and find the class topper.

---

## ▶️ How to Run

Run any file using:

```bash
python filename.py
```

Example:

```bash
python 01-what-is-lambda.py
python 06-mini_project.py
```

---

## 🧠 Important Concepts and Syntax

```python
# Basic lambda syntax
lambda arguments: expression

# Examples
square = lambda num: num * num
add = lambda a, b: a + b
power = lambda base, exponent=2: base ** exponent

# Conditional (ternary) expression inside a lambda
label = lambda n: "positive" if n > 0 else "negative"

# Passing a lambda directly to sorted()
ranked = sorted(students, key=lambda s: s["marks"])
```

Python looks for the `key` value to know how to sort or compare items.
The lambda simply tells Python *which value to look at*.

---

## ⚠️ Common Mistakes and Debugging Tips

1. **Writing complex logic in a lambda**
   If your lambda needs many `if/else` branches, use a normal `def` function.
   Lambdas are for one simple expression.

2. **Forgetting that a lambda returns the expression result**
   `lambda x: x + 1` already returns the value — do not write `return` inside.

3. **Using a lambda where a named function is clearer**
   If you assign a lambda to a name and reuse it everywhere, a `def` function
   is usually better style.

---

## 🏋️ Practice Exercises

1. Write a lambda that takes a string and returns its length.
2. Write a lambda that takes a number and returns `True` if it is even.
3. Use `sorted()` with a lambda to sort a list of words by their length.
4. Modify the Grade Analyzer project to also print the subject-wise
   highest scorer.

---

## 🧩 Mini Project: Grade Analyzer

**File:** `06-mini_project.py`

This project uses lambda functions to process a list of students:

1. Calculates each student's average marks with a lambda
2. Ranks students by average (highest first) using `sorted()` + lambda
3. Assigns grade labels (A–F) using a conditional lambda
4. Finds the class topper using `max()` + lambda

Run it and try adding more students or subjects to the data.

---

## 📚 Official Python Documentation

- Lambda Expressions  
  https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

- `sorted()`  
  https://docs.python.org/3/library/functions.html#sorted

---

© 2026 ISTMX. All rights reserved.

ISTMX — Python Learning Resource  
Aryan — Developer & Maintainer
