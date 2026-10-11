# File Handling 📁

This folder introduces **file handling** in Python — how programs
read from and write to files so data persists after the program ends.

Files let programs remember information: notes, logs, contacts,
marks, and more.

---

## 🧠 What Is File Handling?

**File handling** means opening a file, reading or writing its
content, and closing it.

```python
# The modern, recommended way: the 'with' statement
with open("data.txt", "r") as file:
    content = file.read()
# the file is closed automatically here
```

---

## 🎯 Why File Handling Matters

File handling lets your programs:
- save data permanently (contacts, scores, settings)
- read configuration and data files
- work with logs, CSV exports, and reports
- build real applications that remember things

---

## 📂 Files in This Folder

1. **`01-opening-and-reading-files.py`**
   Opening files with `open()`, reading with `read()`,
   closing files, and rewinding with `seek(0)`.

2. **`02-writing-to-files.py`**
   Writing with mode `"w"` (and its erasing behavior),
   `write()` vs `writelines()`, and converting numbers to strings.

3. **`03-appending-to-files.py`**
   Adding content with mode `"a"` — perfect for logs.

4. **`04-with-statement.py`**
   The `with` statement: automatic closing, even on errors,
   and opening multiple files at once.

5. **`05-reading-line-by-line.py`**
   Three ways to read line by line, plus a practical
   example that parses and averages marks.

6. **`06-file-modes-explained.py`**
   A complete tour of modes: `r`, `w`, `a`, `x`, `r+`, and `b`.

7. **`07-working-with-csv-files.py`**
   Reading and writing CSV files with the `csv` module,
   including `DictReader` for dictionary-style access.

8. **`08-mini_project.py`**
   A Contact Book mini project that saves contacts to
   `contacts.txt` between runs.

---

## ▶️ How to Run

Run any file using (from inside this folder):

```bash
python filename.py
```

Example:

```bash
python 01-opening-and-reading-files.py
python 08-mini_project.py
```

Note: the example scripts create small demo files
(`demo_notes.txt`, `output.txt`, `marks.csv`, etc.) in the
current folder while running. The Contact Book creates
`contacts.txt`. These are safe to delete.

---

## 🧠 Important Concepts and Syntax

```python
# Modes
open("file.txt", "r")    # read (default)
open("file.txt", "w")    # write (erases!)
open("file.txt", "a")    # append
open("file.txt", "x")    # create only if missing

# Reading
file.read()              # entire file as one string
file.readline()          # one line
file.readlines()         # list of all lines

# Writing
file.write("text\n")     # one string (add \n yourself)
file.writelines(["a\n", "b\n"])

# Always prefer 'with' — it closes the file automatically
with open("file.txt", "r") as file:
    data = file.read()
```

---

## ⚠️ Common Mistakes and Debugging Tips

1. **Forgetting to close files**
   Use `with` — it closes files automatically, even on errors.

2. **Using "w" when you meant "a"**
   `"w"` erases the whole file. Use `"a"` to add to it.

3. **FileNotFoundError**
   The file does not exist in the current folder.
   Check the filename and your working directory.

4. **TypeError: write() takes strings only**
   Convert numbers first: `file.write(str(42))`.

5. **Newlines on Windows**
   When writing CSV, open with `newline=""` to avoid blank rows.

---

## 🏋️ Practice Exercises

1. Write a program that saves your favorite quotes to a file,
   one per line, and reads them back.
2. Create a program that counts how many times each word
   appears in a text file.
3. Write a program that copies the content of one file to another.
4. Add error handling to exercise 3 for missing files.
5. Extend the Contact Book with an "edit contact" option.

---

## 🧩 Mini Project: Contact Book

**File:** `08-mini_project.py`

This project builds a persistent contact book:

1. Loads contacts from `contacts.txt` on startup
2. Handles `FileNotFoundError` gracefully on first run
3. Supports view, add, search, and delete operations
4. Saves contacts back to the file after every change

Run it, add some contacts, close the program, and run it again —
your contacts are still there.

---

## 📚 Official Python Documentation

- Reading and Writing Files (Python Tutorial)  
  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

- `csv` — CSV File Reading and Writing  
  https://docs.python.org/3/library/csv.html

---

© 2026 ISTMX. All rights reserved.

ISTMX — Python Learning Resource  
Aryan — Developer & Maintainer
