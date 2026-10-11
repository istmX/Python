# Modules and Packages 📦

This folder introduces **modules** and **packages** — Python's way
of organizing code into reusable files and folders.

Instead of one giant file, real programs are split into modules
that import each other.

---

## 🧠 What Are Modules and Packages?

- A **module** is a single `.py` file with functions, classes, or variables
- A **package** is a folder of modules (with an `__init__.py` file)
- The **standard library** is the collection of modules Python ships with

```python
import math                 # use a built-in module
from math import pi        # import one name
import random as rnd       # import with an alias
```

---

## 🎯 Why Modules Matter

Modules help you:
- reuse code without copying it
- keep programs organized and readable
- share code between projects
- use the huge Python standard library (no installation needed)

---

## 📂 Files in This Folder

1. **`01-what-are-modules.py`**
   What modules are, with built-in examples (`math`, `random`).

2. **`02-importing-modules.py`**
   The four import styles: whole module, specific names,
   aliases, and why `import *` is discouraged.

3. **`03-from-import-as.py`**
   `from ... import ... as ...` for short names and avoiding clashes.

4. **`04-standard-library-modules.py`**
   A tour of useful built-in modules: `math`, `random`,
   `datetime`, `os`, and `sys`.

5. **`calculator_helpers.py`**
   A custom module (our own file) with calculator functions.
   This is the module imported by the next file.

6. **`05-creating-your-own-module.py`**
   How to import and use your own module, including error handling.

7. **`06-what-are-packages.py`**
   What packages are and how to import from them using the
   `geometry` package included in this folder.

8. **`07-the-main-guard.py`**
   The `if __name__ == "__main__":` guard that prevents code
   from running when a file is imported.

9. **`08-mini_project.py`**
   A Geometry Calculator mini project that uses the custom
   `geometry` package with validated user input.

**The `geometry/` package:**
- `geometry/__init__.py` — package marker, exposes `PI`
- `geometry/circle.py` — circle area and circumference
- `geometry/rectangle.py` — rectangle area and perimeter

---

## ▶️ How to Run

Run any file using (from inside this folder):

```bash
python filename.py
```

Example:

```bash
python 01-what-are-modules.py
python 05-creating-your-own-module.py
python 08-mini_project.py
```

The mini project is interactive — it asks for a shape and dimensions.

---

## 🧠 Important Concepts and Syntax

```python
# Import styles
import math
from math import pi, sqrt
import random as rnd
from math import factorial as fact

# Your own module (calculator_helpers.py in this folder)
import calculator_helpers
calculator_helpers.add(2, 3)

# Your own package (geometry/ in this folder)
from geometry.circle import area

# The main guard
if __name__ == "__main__":
    main()
```

---

## ⚠️ Common Mistakes and Debugging Tips

1. **ModuleNotFoundError**
   The file you are importing is not in the same folder
   (or not installed). Check the filename spelling and location.

2. **Import runs unwanted code**
   Top-level code in a module runs on import. Put demo/test code
   inside `if __name__ == "__main__":`.

3. **Name clashes**
   Your file named `random.py` would shadow the standard `random`
   module. Never name your files after standard library modules.

4. **Missing `__init__.py`**
   Packages need an `__init__.py` file (it can be empty) so Python
   treats the folder as a package.

5. **Circular imports**
   Module A imports B while B imports A. Restructure to avoid this.

---

## 🏋️ Practice Exercises

1. Create a module `temperature.py` with functions to convert
   Celsius to Fahrenheit and back. Import and use it in another file.
2. Use the `datetime` module to print the current date in the
   format `DD-MM-YYYY`.
3. Use the `random` module to build a simple dice-rolling game.
4. Add a `triangle.py` module to the `geometry` package with
   area and perimeter functions.
5. Add input validation to the Geometry Calculator for menu choices.

---

## 🧩 Mini Project: Geometry Calculator

**File:** `08-mini_project.py`

This project uses the custom `geometry` package:

1. Shows a menu (circle / rectangle / exit)
2. Validates all user input (positive numbers only)
3. Calculates area and perimeter/circumference
4. Uses the `if __name__ == "__main__":` guard

Run it and try adding a triangle option.

---

## 📚 Official Python Documentation

- Modules (Python Tutorial)  
  https://docs.python.org/3/tutorial/modules.html

- The Python Standard Library  
  https://docs.python.org/3/library/index.html

- `if __name__ == "__main__"` explanation  
  https://docs.python.org/3/library/__main__.html

---

© 2026 ISTMX. All rights reserved.

ISTMX — Python Learning Resource  
Aryan — Developer & Maintainer
