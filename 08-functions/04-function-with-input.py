# Functions can also contain input statements
# This helps group related logic together

def user_info():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    
    print("Name:", name)
    print("Age:", age)

# Calling the function to run the code inside it
user_info()
