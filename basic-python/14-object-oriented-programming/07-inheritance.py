# Inheritance
# Inheritance lets a new class reuse and extend an existing class.
# The new class is called the child (subclass), the old one the
# parent (superclass).

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

    def eat(self):
        print(f"{self.name} is eating.")


# Child classes inherit everything from Animal
class Dog(Animal):
    def fetch(self):
        print(f"{self.name} fetches the ball.")


class Cat(Animal):
    def climb(self):
        print(f"{self.name} climbs a tree.")


# Child objects can use their own methods AND the parent's methods
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()    # Buddy makes a sound.   (from Animal)
dog.eat()      # Buddy is eating.       (from Animal)
dog.fetch()    # Buddy fetches the ball. (Dog's own)

cat.speak()    # Whiskers makes a sound.
cat.climb()    # Whiskers climbs a tree.

# isinstance() checks the inheritance relationship
print(isinstance(dog, Dog))      # True
print(isinstance(dog, Animal))   # True
print(isinstance(dog, Cat))      # False

# Overriding: a child can replace a parent method with its own version
class Cow(Animal):
    def speak(self):
        print(f"{self.name} says Moo!")

cow = Cow("Bella")
cow.speak()    # Bella says Moo!  (overridden version)
