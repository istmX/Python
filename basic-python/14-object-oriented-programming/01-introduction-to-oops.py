# Introduction to Object-Oriented Programming (OOP)
# OOP is a way of organizing code around "objects" that combine
# data (attributes) and behavior (methods).

# Real-life analogy:
#   A "Dog" is a class (a blueprint).
#   Your pet dog "Buddy" is an object (a real thing built from that blueprint).
#   Attributes: name, age, breed.
#   Methods: bark(), eat(), sleep().

# Why OOP?
# - Groups related data and functions together
# - Makes code easier to reuse and extend
# - Models real-world things naturally

# Without OOP: data and functions are separate
student_name = "Aryan"
student_marks = 88

def print_student(name, marks):
    print(name, "scored", marks)

print_student(student_name, student_marks)

# With OOP: data and behavior live together in one object
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def print_result(self):
        print(self.name, "scored", self.marks)

student = Student("Aryan", 88)
student.print_result()

# The OOP version keeps everything about a student in one place.
# As programs grow, this organization becomes very valuable.
