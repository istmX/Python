# Raising Exceptions
# You can raise exceptions yourself when something is wrong.
# Use 'raise' to signal an error condition.

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    if amount > balance:
        raise ValueError("Insufficient balance.")
    return balance - amount


# Test the function with invalid input
try:
    new_balance = withdraw(1000, -50)
except ValueError as error:
    print("Transaction failed:", error)

try:
    new_balance = withdraw(1000, 5000)
except ValueError as error:
    print("Transaction failed:", error)

# Valid call
new_balance = withdraw(1000, 300)
print("New balance:", new_balance)

# Raising stops the function immediately — like return,
# but it hands control to the nearest except block.
# If no except block catches it, the program crashes with a traceback.
