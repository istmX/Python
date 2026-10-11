# Classes and Objects
# A class is a blueprint. An object is built from that blueprint.

class Dog:
    # A method is a function defined inside a class
    def bark(self):
        print("Woof! Woof!")

    def describe(self):
        print("I am a dog.")

# Create objects (instances) from the class
buddy = Dog()
maxx = Dog()

# Each object can use the class's methods
buddy.bark()
maxx.bark()
buddy.describe()

# buddy and maxx are DIFFERENT objects.
# They share the same blueprint but are separate things.
print("buddy is maxx:", buddy is maxx)   # False

# Every object knows its class
print("buddy's class:", type(buddy))

# You can create as many objects as you want from one class
dogs = [Dog(), Dog(), Dog()]
for dog in dogs:
    dog.bark()
