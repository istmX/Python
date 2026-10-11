# Combining map, filter, and reduce
# These tools work beautifully together as a pipeline:
#   1. filter  -> select the items you need
#   2. map     -> transform them
#   3. reduce  -> combine into a final result

from functools import reduce

# Example: total price of all products that cost more than 100
products = [
    {"name": "Pen", "price": 20},
    {"name": "Notebook", "price": 150},
    {"name": "Bag", "price": 500},
    {"name": "Pencil", "price": 10},
    {"name": "Calculator", "price": 300},
]

# Step 1: filter — keep only expensive products
expensive = list(filter(lambda p: p["price"] > 100, products))
print("Expensive products:", [p["name"] for p in expensive])

# Step 2: map — extract just their prices
prices = list(map(lambda p: p["price"], expensive))
print("Their prices:", prices)

# Step 3: reduce — add the prices together
total = reduce(lambda a, b: a + b, prices, 0)
print("Total price:", total)

# The whole pipeline in one expression:
total_one_liner = reduce(
    lambda a, b: a + b,
    map(lambda p: p["price"], filter(lambda p: p["price"] > 100, products)),
    0,
)
print("Same result in one line:", total_one_liner)

# Note: for simple cases, a loop or comprehension may read better.
# Pipelines like this shine when each step is simple and clear.
