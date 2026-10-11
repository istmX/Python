# Python Scope 🔍

This folder introduces **scope in Python** — the rules that decide
where a variable can be seen and used.

Understanding scope prevents many common bugs, such as
"variable not defined" errors or functions that fail to update values.

---

## 🧠 What Is Scope?

**Scope** is the region of a program where a variable is visible.

Python follows the **LEGB rule** when looking up a name:

1. **L**ocal — inside the current function
2. **E**nclosing — inside any enclosing (outer) function
3. **G**lobal — at the top level of the file
4. **B**uilt-in — names Python provides (`print`, `len`, ...)

Python searches in that order and uses the first match it finds.

---

## 🎯 Why Scope Matters

Scope matters because it:
- decides which variables a function can read or change
- prevents two functions from accidentally overwriting each other's data
- explains why some variables "disappear" after a function ends

---

## 📂 Files in This Folder

1. **`01-what-is-scope.py`**
   The four scopes and the LEGB rule, with a local and a global example.

2. **`02-local-scope.py`**
   Variables created inside a function belong to it only.
   Shows that separate functions can reuse the same variable name safely.

3. **`03-global-scope.py`**
   Global variables can be read anywhere, but assigning to them
   inside a function silently creates a new local variable instead.

4. **`04-global-keyword.py`**
   How `global` lets a function change a global variable,
   plus the cleaner alternative (parameters + return).

5. **`05-nonlocal-keyword.py`**
   How `nonlocal` lets a nested function change a variable
   from its enclosing function.

6. **`06-common-mistakes.py`**
   The three most common scope mistakes: using a variable before
   assigning it, expecting globals to change by default, and shadowing.

7. **`07-mini_project.py`**
   A Game Score Tracker mini project that uses `global` to update
   shared game state and a nested function to demonstrate enclosing scope.

---

## ▶️ How to Run

Run any file using:

```bash
python filename.py
```

Example:

```bash
python 01-what-is-scope.py
python 07-mini_project.py
```

---

## 🧠 Important Concepts and Syntax

```python
# Local variable: exists only inside the function
def my_function():
    local_var = 10

# Global variable: exists at the top level of the file
global_var = 10

def change_global():
    global global_var        # declare it first
    global_var = 20          # now this changes the global

def outer():
    outer_var = 1
    def inner():
        nonlocal outer_var   # refers to outer()'s variable
        outer_var = 2
```

---

## ⚠️ Common Mistakes and Debugging Tips

1. **"UnboundLocalError"** — you tried to read a variable before assigning it
   inside a function. Fix: assign it first, or declare `global`.

2. **Function did not update my variable** — assigning to a name inside a
   function creates a local copy. Fix: use `global`, or better, return the
   new value and store it.

3. **Shadowing** — a local variable hides a global with the same name.
   Fix: use clear, different names.

4. **Too many globals** — code with many global variables is hard to debug.
   Fix: pass values as parameters and return results instead.

---

## 🏋️ Practice Exercises

1. Predict the output of a function that prints a variable defined outside it.
2. Write a function that tries to change a global without `global` and
   observe what happens. Then fix it with `global`.
3. Write a nested function that changes an outer variable using `nonlocal`.
4. Add a "high score" feature to the Score Tracker project.

---

## 🧩 Mini Project: Game Score Tracker

**File:** `07-mini_project.py`

This project simulates a small game:

1. Plays three rounds, updating global score variables with `global`
2. Shows player stats (games played, total score, average)
3. Resets the game, with a nested function demonstrating enclosing scope

Run it and try adding more rounds or a second player.

---

## 📚 Official Python Documentation

- Python Scopes and Namespaces  
  https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces

- The `global` statement  
  https://docs.python.org/3/reference/simple_stmts.html#the-global-statement

- The `nonlocal` statement  
  https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement

---

© 2026 ISTMX. All rights reserved.

ISTMX — Python Learning Resource  
Aryan — Developer & Maintainer
