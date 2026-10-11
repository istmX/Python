# Lambda vs Regular Function
# Both do the same job. The difference is style and where you use them.

# Regular function: good for complex, reusable logic
def add_regular(a, b):
    return a + b

# Lambda: good for short, one-line logic
add_lambda = lambda a, b: a + b

print("Regular function:", add_regular(3, 4))
print("Lambda function:", add_lambda(3, 4))

# When should you use which?
#
# Use a regular function when:
# - the logic has multiple steps
# - you need comments/docstrings inside
# - you will reuse it in many places
#
# Use a lambda when:
# - the logic is a single simple expression
# - you pass it directly to another function (we will see this soon)

# Common mistake: assigning a lambda to a name and using it everywhere.
# That is fine, but a regular function is usually clearer:
#
#   double = lambda x: x * 2     # works
#   def double(x): return x * 2 # clearer for reusable code

print("Double with lambda:", (lambda x: x * 2)(10))
