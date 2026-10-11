# Mini Project: Shopping Cart Processor
# This project uses map, filter, and reduce to process cart data.

from functools import reduce

# Each product: name, price, and quantity in the cart
cart = [
    {"name": "Pen", "price": 20, "quantity": 3},
    {"name": "Notebook", "price": 150, "quantity": 2},
    {"name": "Bag", "price": 500, "quantity": 1},
    {"name": "Pencil", "price": 10, "quantity": 5},
    {"name": "Calculator", "price": 300, "quantity": 1},
]

DISCOUNT_RATE = 0.10   # 10% discount
FREE_SHIPPING_LIMIT = 1000

print("=" * 45)
print("SHOPPING CART PROCESSOR")
print("=" * 45)

# 1. map: calculate the line total (price * quantity) for each item
line_totals = list(map(lambda item: item["price"] * item["quantity"], cart))
print("\nLine totals:", line_totals)

# 2. reduce: compute the grand total
grand_total = reduce(lambda a, b: a + b, line_totals, 0)
print("Grand total:", grand_total)

# 3. map: apply a 10% discount to each line total
discounted_totals = list(map(lambda total: total * (1 - DISCOUNT_RATE), line_totals))
print("Discounted totals:", [round(t, 2) for t in discounted_totals])

# 4. reduce: total after discount
total_after_discount = reduce(lambda a, b: a + b, discounted_totals, 0)
print("Total after discount:", round(total_after_discount, 2))

# 5. filter: find items with a line total above 100
big_items = list(filter(lambda item: item["price"] * item["quantity"] > 100, cart))
print("\nItems above 100:")
for item in big_items:
    print(f"  {item['name']}: {item['price'] * item['quantity']}")

# 6. map: build a receipt line for each item
receipt_lines = list(
    map(
        lambda item: f"{item['name']}: {item['price']} x {item['quantity']}",
        cart,
    )
)
print("\n--- Receipt ---")
for line in receipt_lines:
    print(line)

# 7. Shipping decision
shipping = 0 if grand_total >= FREE_SHIPPING_LIMIT else 50
print(f"\nShipping: {shipping}")
print(f"FINAL BILL: {round(total_after_discount + shipping, 2)}")

print("\n" + "=" * 45)
