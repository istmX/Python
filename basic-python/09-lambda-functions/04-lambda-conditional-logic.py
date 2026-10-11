# Conditional Logic Inside a Lambda
# A lambda can make decisions using a ternary expression:
#   value_if_true if condition else value_if_false

# Check if a number is positive, negative, or zero
check = lambda n: "positive" if n > 0 else "negative" if n < 0 else "zero"

print(check(10))   # positive
print(check(-5))   # negative
print(check(0))    # zero

# Grade label example
grade_label = lambda marks: "pass" if marks >= 33 else "fail"

print(grade_label(75))  # pass
print(grade_label(20))  # fail

# Common mistake: lambdas get hard to read with too many conditions.
# If you need many conditions, use a regular function instead.
#
#   label = lambda n: "a" if n == 1 else "b" if n == 2 else "c" if n == 3 else "?"
#
# That works, but a def function with if/elif is much easier to read.
