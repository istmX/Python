# return is used to SEND a value back from a function
# It is different from print

def square(num):
    # This value will be returned to the caller
    return num * num

# Store the returned value in a variable
result = square(5)

print("Square:", result)
