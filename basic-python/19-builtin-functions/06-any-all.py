# any() and all() — Check Conditions Across Items

# all() returns True only if EVERY item is truthy
print(all([True, True, True]))      # True
print(all([True, False, True]))     # False

# any() returns True if AT LEAST ONE item is truthy
print(any([False, False, True]))    # True
print(any([False, False, False]))   # False

# Practical: validate marks
marks = [88, 95, 72]
print("All marks positive?", all(m > 0 for m in marks))       # True
print("Any mark above 90?", any(m > 90 for m in marks))       # True

# Check if all inputs meet a requirement
ages = [18, 21, 19, 25]
print("All adults?", all(age >= 18 for age in ages))          # True

# Truthiness reminders:
# Falsy values: 0, "", [], {}, None, False
# Everything else is truthy
print(all(["a", "b", ""]))          # False ("" is falsy)
print(any([0, 0, 1]))               # True (1 is truthy)

# Empty collections:
print(all([]))      # True  (vacuously true)
print(any([]))      # False (nothing to satisfy the condition)

# These are perfect for clean validation code — no loops needed.
