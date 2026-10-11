# Constructors and __init__
# The constructor is a special method that runs automatically
# when you create an object. In Python it is called __init__.

class Student:
    # self refers to the object being created
    def __init__(self, name, marks):
        # Store the passed values as attributes of the object
        self.name = name
        self.marks = marks
        print(f"Student created: {name}")

    def print_result(self):
        print(f"{self.name} scored {self.marks} marks")

# Python calls __init__ automatically with the arguments you pass
student_one = Student("Aryan", 88)     # Student created: Aryan
student_two = Student("Priya", 95)     # Student created: Priya

student_one.print_result()   # Aryan scored 88 marks
student_two.print_result()   # Priya scored 95 marks

# Each object stores its OWN data
print(student_one.name)   # Aryan
print(student_two.name)   # Priya

# Key points about __init__:
# - It is called automatically on creation
# - 'self' is passed automatically — you never pass it yourself
# - It is the right place to set up the object's initial state
# - The name must be exactly __init__ (double underscores both sides)
