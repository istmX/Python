# Instance Variables and Class Variables
# Instance variables: unique to each object.
# Class variables: shared by all objects of the class.

class Dog:
    # Class variable: shared by every Dog object
    species = "Canis familiaris"
    count = 0          # how many dogs have been created

    def __init__(self, name, age):
        # Instance variables: unique to each object
        self.name = name
        self.age = age
        Dog.count = Dog.count + 1

    def describe(self):
        print(f"{self.name} is {self.age} years old ({self.species})")

# Create two dogs
buddy = Dog("Buddy", 3)
maxx = Dog("Max", 5)

# Instance variables differ per object
buddy.describe()   # Buddy is 3 years old (Canis familiaris)
maxx.describe()    # Max is 5 years old (Canis familiaris)

# Class variables are the same for everyone
print(buddy.species)   # Canis familiaris
print(maxx.species)    # Canis familiaris
print("Dogs created:", Dog.count)   # 2

# You can access class variables through the class itself
print(Dog.species)     # Canis familiaris

# ⚠️ Careful: assigning through an INSTANCE creates a new
# instance variable that shadows the class variable.
buddy.species = "Felis catus"   # only buddy changes!
print(buddy.species)   # Felis catus (instance variable now)
print(maxx.species)    # Canis familiaris (still the class variable)
print(Dog.species)     # Canis familiaris (class variable unchanged)
