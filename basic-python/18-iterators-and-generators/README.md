# Iterators and Generators 🔁

This folder introduces **iterators** and **generators** — Python's
tools for producing items one at a time, without holding everything
in memory.

---

## 🧠 What Are Iterators and Generators?

- An **iterator** is an object that produces items one by one
  (using `iter()` and `next()`)
- A **generator** is a easy way to create iterators using `yield`

```python
def countdown(start):
    while start > 0:
        yield start      # produce one item, pause, resume later
        start = start - 1

for number in countdown(5):
    print(number)        # 5 4 3 2 1
```

---

## 🎯 Why Iterators and Generators Matter

They help you:
- process huge datasets with almost no memory
- represent infinite sequences (counters, streams)
- write cleaner, more Pythonic code for iteration
- build data pipelines step by step

---

## 📂 Files in This Folder

1. **`01-what-are-iterators.py`**
   What iterators are, `iter()`, and how for loops use them.

2. **`02-iter-and-next.py`**
   `next()` in detail, `StopIteration`, and the default-value form
   of `next()`.

3. **`03-creating-custom-iterator.py`**
   Building a class with `__iter__()` and `__next__()` so it works
   with for loops and `next()`.

4. **`04-what-are-generators.py`**
   Generator functions with `yield`, lazy evaluation, and the
   memory-efficiency benefit.

5. **`05-yield-keyword.py`**
   How `yield` pauses and resumes functions, `yield` vs `return`,
   and infinite generators.

6. **`06-generator-expressions.py`**
   `(x for x in ...)` syntax, comparison with list comprehensions,
   and use inside `sum()` / `max()`.

7. **`07-iterator-vs-generator.py`**
   The same task solved with an iterator class and a generator,
   with guidance on choosing.

8. **`08-mini_project.py`**
   A Generator Toolbox mini project: a Fibonacci generator, a
   custom range generator, and a memory-safe chunked file reader.

---

## ▶️ How to Run

Run any file using:

```bash
python filename.py
```

Example:

```bash
python 03-creating-custom-iterator.py
python 08-mini_project.py
```

The mini project creates a `big_sample.txt` demo file — safe to delete.

---

## 🧠 Important Concepts and Syntax

```python
# iterables produce iterators
iterator = iter([1, 2, 3])
next(iterator)                 # 1

# custom iterator class
class MyIterator:
    def __iter__(self):
        return self
    def __next__(self):
        # return next item or raise StopIteration
        pass

# generator function
def my_generator():
    yield 1
    yield 2

# generator expression
squares = (n * n for n in range(10))
```

Key difference:
- `return` ends a function forever
- `yield` pauses it and resumes on the next `next()` call

---

## ⚠️ Common Mistakes and Debugging Tips

1. **StopIteration when calling next() manually**
   The generator is exhausted. Loop with `for` instead, or recreate it.

2. **Reusing a generator**
   Generators are one-time use. After a full loop, a generator is empty.
   Call the function again to get a fresh one.

3. **Forgetting the counter update in custom iterators**
   Without moving toward the base condition, for loops never stop.

4. **Using a list when a generator fits**
   `(n * n for n in range(1000000))` uses almost no memory;
   `[n * n for n in range(1000000)]` stores a million numbers.

5. **Debugging tip** — convert to a list to inspect:
   `print(list(my_generator()))` (only for small generators).

---

## 🏋️ Practice Exercises

1. Write a generator that yields even numbers up to a given limit.
2. Write a generator that yields the letters of a word one by one.
3. Create a custom iterator class for the days of the week.
4. Write a generator expression that yields the lengths of all words
   in a sentence.
5. Add a generator to the Toolbox that yields prime numbers up to a limit.

---

## 🧩 Mini Project: Generator Toolbox

**File:** `08-mini_project.py`

This project bundles three generator tools:

1. **Fibonacci generator** — yields the first N Fibonacci numbers
2. **Custom range** — a hand-written version of `range()` using `yield`
3. **Chunked file reader** — reads a file a few lines at a time,
   keeping memory usage low for very large files, with
   `FileNotFoundError` handling

Run it and try the tools with your own inputs.

---

## 📚 Official Python Documentation

- Iterators (Python Tutorial)  
  https://docs.python.org/3/tutorial/classes.html#iterators

- Generators (Python Tutorial)  
  https://docs.python.org/3/tutorial/classes.html#generators

- Generator Expressions  
  https://docs.python.org/3/tutorial/classes.html#generator-expressions

---

© 2026 ISTMX. All rights reserved.

ISTMX — Python Learning Resource  
Aryan — Developer & Maintainer
