# Abstraction
# Abstraction means hiding complex details and showing only
# what is necessary. You use the class without knowing HOW
# it works inside.

# Example: you drive a car. You use the steering wheel and pedals.
# You do not need to know how the engine works. That is abstraction.

# In Python, abstract classes (using the abc module) define
# methods that every child class MUST implement.

from abc import ABC, abstractmethod


# Abstract class: cannot be used to create objects directly
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass    # no body here — children must provide it

    @abstractmethod
    def perimeter(self):
        pass


# Concrete classes implement the abstract methods
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius


# shape = Shape()   # ERROR: cannot create an abstract class object

rectangle = Rectangle(5, 3)
circle = Circle(4)

print("Rectangle area:", rectangle.area())            # 15
print("Rectangle perimeter:", rectangle.perimeter())  # 16
print("Circle area:", round(circle.area(), 2))        # 50.27
print("Circle perimeter:", round(circle.perimeter(), 2))  # 25.13

# The user of a Shape only cares about area() and perimeter().
# How each shape calculates them is hidden (abstracted away).
