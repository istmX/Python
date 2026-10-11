# Functional Programming Tools: map, filter, reduce 🛠️

This folder introduces Python's functional programming tools:
**`map()`**, **`filter()`**, and **`reduce()`**.

These functions process collections by applying a function to each
item — without writing an explicit loop.

---

## 🧠 What Are map, filter, and reduce?

| Tool      | Job                                      |
|-----------|------------------------------------------|
| `map()`   | Transform every item                     |
| `filter()` | Keep only items that match a condition  |
| `reduce()` | Combine all items into a single value   |

- `map()` and `filter()` are built-in functions
- `reduce()` must be imported: `from functools import reduce`

```python
numbers = [1, 2, 3, 4, 5]

list(map(lambda n: n * 2, numbers))           # [2, 4, 6, 8, 10]
list(filter(lambda n: n % 2 == 0, numbers))  # [2, 4]
reduce(lambda a, b: a + b, numbers, 0)       # 15
```

---

## 🎯 Why These Tools Matter

They help you:
- process data in clear, named steps (transform, filter, combine)
- build pipelines where data flows through simple functions
- write code that expresses *what* to do, not *how* to loop

---

## 📂 Files in This Folder

1. **`01-functional-programming-intro.py`**
   Overview of the three tools and a first example of each.

2. **`02-map-function.py`**
   `map()` with built-in functions, lambdas, named functions,
   and multiple iterables.

3. **`03-filter-function.py`**
   `filter()` with conditions, truthy filtering with `None`,
   and named predicate functions.

4. **`04-reduce-function.py`**
   `reduce()` for sums, products, maximums, joining strings,
   and using an initial value.

5. **`05-combining-map-filter-reduce.py`**
   Chaining the three tools into a data-processing pipeline.

6. **`06-functional-vs-loops.py`**
   The same task solved three ways (loop, comprehension,
   functional pipeline) with guidance on choosing a style.

7. **`07-mini_project.py`**
   A Shopping Cart Processor mini project that uses all three
   tools to compute totals, discounts, and a final bill.

---

## ▶️ How to Run

Run any file using:

```bash
python filename.py
```

Example:

```bash
python 01-functional-programming-intro.py
python 07-mini_project.py
```

---

## 🧠 Important Concepts and Syntax

```python
from functools import reduce

# map: transform each item
doubled = list(map(lambda n: n * 2, numbers))

# filter: keep items that satisfy a condition
evens = list(filter(lambda n: n % 2 == 0, numbers))

# reduce: combine everything into one value
total = reduce(lambda a, b: a + b, numbers, 0)

# Pipeline: filter -> map -> reduce
result = reduce(lambda a, b: a + b,
                map(lambda n: n * n,
                    filter(lambda n: n % 2 == 0, numbers)),
                0)
```

Important details:
- `map()` and `filter()` return iterators — wrap them in `list()` to see the values
- `reduce()` needs an initial value for empty-list safety
- `map()` with multiple iterables stops at the shortest one

---

## ⚠️ Common Mistakes and Debugging Tips

1. **Forgetting `list()` around map/filter**
   Printing a map object shows `<map object at 0x...>`.
   Use `list(...)` to see the actual values.

2. **Forgetting to import reduce**
   `reduce` is not built-in. Always write `from functools import reduce`.

3. **TypeError on empty lists with reduce**
   Without an initial value, `reduce()` fails on empty lists.
   Pass one: `reduce(fn, items, 0)`.

4. **Over-chaining**
   A pipeline of three nested functions can become hard to read.
   Break it into named steps or use a comprehension.

---

## 🏋️ Practice Exercises

1. Use `map()` to convert a list of prices from strings to floats.
2. Use `filter()` to keep only words longer than 5 letters.
3. Use `reduce()` to find the longest word in a list.
4. Write a pipeline that computes the average of all numbers
   greater than 10 in a list.
5. Add a "remove item" feature to the Shopping Cart project.

---

## 🧩 Mini Project: Shopping Cart Processor

**File:** `07-mini_project.py`

This project processes a shopping cart with functional tools:

1. `map()` computes each line total (price × quantity)
2. `reduce()` computes the grand total
3. `map()` applies a 10% discount
4. `filter()` finds items above 100
5. `map()` builds receipt lines
6. Shipping is added and the final bill is printed

Run it and try changing the discount rate or adding new products.

---

## 📚 Official Python Documentation

- `map()`  
  https://docs.python.org/3/library/functions.html#map

- `filter()`  
  https://docs.python.org/3/library/functions.html#filter

- `functools.reduce()`  
  https://docs.python.org/3/library/functools.html#functools.reduce

---

© 2026 ISTMX. All rights reserved.

ISTMX — Python Learning Resource  
Aryan — Developer & Maintainer
