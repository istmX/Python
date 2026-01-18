# Python Basics

This folder introduces the most important concepts required to start programming in Python.

The goal of this folder is to build a strong foundation before moving to logic, conditions, and projects.

---

## 🧵 What Are Strings?

A **string** is a sequence of characters.

In simple words:
- Anything written inside quotes is a string
- Strings are used to store text

Examples:
- "Hello"
- "Python"
- "My name is Alex"

Strings are mainly used for:
- user input
- messages
- program output
- interaction with users

---

## ✍️ Creating Strings

Strings can be created using:
- Double quotes `" "`
- Single quotes `' '`

Example:
name = "Python"
message = 'Hello World'


---

## 🔤 Important String Methods

Python provides built-in methods to work with strings.

These methods do **not** change the original string.  
They return a new string instead.

---

### `upper()`
Converts the string to uppercase.

Example:
name.upper()


---

### `lower()`
Converts the string to lowercase.

Example:
name.lower()


---

### `len()`
Returns the number of characters in a string.

Example:
len(name)

---

## 🚪 Escape Sequence Characters

Sometimes we want special formatting inside strings.

Python uses **escape sequences** for this.

Escape sequences start with a **backslash (`\`)**.

---

### `\n` → New Line
Moves text to the next line.

Example:
print("Hello\nWorld")

Output:
Hello
World


---

### `\t` → Tab Space
Adds horizontal spacing.

Example:
print("Name\tAge")


---

### `\"` → Double Quote
Used to print double quotes inside a string.

Example:
print("He said "Hello"")


---

### `\'` → Single Quote
Used to print single quotes inside a string.

Example:
print('It's Python')


---

### `\\` → Backslash
Used to print a backslash.

Example:
print("C:\Users\Python")


---

## 📌 Why Escape Sequences Matter

Escape sequences help in:
- formatting output
- printing menus clearly
- displaying readable messages

They are commonly used with `print()`.

---

## 📂 Files in This Folder

- `input_output.py` → taking input and showing output
- `variables.py` → storing data in variables
- `strings.py` → working with strings and string methods

---

## 📚 Official Python Documentation

These are **original and trusted resources**:

- Python Strings (official docs):  
  https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

- Built-in Functions (`len`, `print`, `input`):  
  https://docs.python.org/3/library/functions.html

- Escape Sequences & String Literals:  
  https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals

---

## 🧠 Learning Tip

Strings are used everywhere in Python.

If you understand strings well, working with:
- conditions
- menus
- projects

becomes much easier later.

Take your time with this topic.
