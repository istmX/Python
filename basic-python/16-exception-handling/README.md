# Exception Handling 🛡️

This folder introduces **exception handling** — how to deal with
errors gracefully so your programs do not crash.

Instead of stopping with a traceback, you can catch errors,
respond to them, and keep running.

---

## 🧠 What Are Exceptions?

An **exception** is an error that occurs while a program runs.

Common built-in exceptions:

| Exception           | When it happens                          |
|---------------------|------------------------------------------|
| `ZeroDivisionError` | Dividing by zero                        |
| `ValueError`        | Right type, wrong value (`int("abc")`)   |
| `TypeError`         | Mixing incompatible types                |
| `NameError`         | Using a variable that does not exist     |
| `KeyError`          | Accessing a missing dictionary key       |
| `IndexError`        | List index out of range                  |
| `FileNotFoundError` | Opening a file that does not exist       |

---

## 🎯 Why Exception Handling Matters

Exception handling helps you:
- keep programs running when something goes wrong
- show friendly error messages instead of crashing
- validate user input safely
- write professional, reliable software

---

## 📂 Files in This Folder

1. **`01-what-are-exceptions.py`**
   What exceptions are and a tour of the common built-in types.

2. **`02-try-except.py`**
   The basic `try / except` structure with division and
   type-conversion examples.

3. **`03-catching-specific-exceptions.py`**
   Why catching everything is bad practice, multiple `except`
   blocks, and using `as error` to read the message.

4. **`04-try-except-else-finally.py`**
   The full structure: `try`, `except`, `else` (no error),
   and `finally` (always runs) with a file example.

5. **`05-raising-exceptions.py`**
   Using `raise` to signal error conditions in your own functions.

6. **`06-common-exception-types.py`**
   A hands-on tour of the seven most common exception types.

7. **`07-user-defined-exceptions.py`**
   Creating your own exception classes by inheriting
   from `Exception`.

8. **`08-mini_project.py`**
   A Student Result System mini project with a custom exception
   and fully validated user input.

---

## ▶️ How to Run

Run any file using:

```bash
python filename.py
```

Example:

```bash
python 02-try-except.py
python 08-mini_project.py
```

The mini project is interactive — try entering text where a
number is expected to see the validation in action.

---

## 🧠 Important Concepts and Syntax

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Success:", result)   # runs only if no error
finally:
    print("Always runs")        # cleanup code

# Raising your own error
raise ValueError("Something is wrong")

# Custom exception
class MyError(Exception):
    pass
```

---

## ⚠️ Common Mistakes and Debugging Tips

1. **Bare `except:` catches everything**
   It hides real bugs like `NameError` from typos.
   Always catch specific exceptions.

2. **Empty except blocks**
   Silently swallowing errors makes debugging impossible.
   At minimum, print the error.

3. **Catching the wrong exception**
   `int("abc")` raises `ValueError`, not `TypeError`.
   Read the traceback to see the actual type.

4. **Forgetting `finally` for cleanup**
   Files and resources should be released in `finally`
   (or better, with `with` — see the file handling topic).

5. **Debugging tip** — let the exception happen on purpose
   to read the full traceback. It tells you the file, line,
   and call stack that led to the error.

---

## 🏋️ Practice Exercises

1. Write a function that divides two numbers and handles both
   `ZeroDivisionError` and `ValueError`.
2. Ask the user for their age and keep asking until they enter
   a valid positive integer.
3. Create a custom `NegativeNumberError` and raise it when a
   function receives a negative number.
4. Write code that opens a file and handles `FileNotFoundError`
   with a friendly message.
5. Add a "retake subject" feature to the Student Result System.

---

## 🧩 Mini Project: Student Result System

**File:** `08-mini_project.py`

This project builds a robust result calculator:

1. A custom `InvalidMarksError` exception for out-of-range marks
2. Input loops that keep asking until valid marks are entered
3. Average and grade calculation
4. A `ZeroDivisionError` guard for empty subject lists

Run it and try entering `abc`, `-5`, or `150` to see the
validation working.

---

## 📚 Official Python Documentation

- Errors and Exceptions (Python Tutorial)  
  https://docs.python.org/3/tutorial/errors.html

- Built-in Exceptions  
  https://docs.python.org/3/library/exceptions.html#built-in-exceptions

---

© 2026 ISTMX. All rights reserved.

ISTMX — Python Learning Resource  
Aryan — Developer & Maintainer
