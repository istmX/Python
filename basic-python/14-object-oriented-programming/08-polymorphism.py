# Polymorphism
# "Polymorphism" means "many forms": the same method name behaves
# differently depending on the object that calls it.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks: Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows: Meow!")


class Cow(Animal):
    def speak(self):
        print(f"{self.name} moos: Moo!")


# The SAME function works with ANY animal — it does not need to
# know which specific animal it received. This is polymorphism.
def make_it_speak(animal):
    animal.speak()


animals = [Dog("Buddy"), Cat("Whiskers"), Cow("Bella")]

for animal in animals:
    make_it_speak(animal)

# Output:
# Buddy barks: Woof!
# Whiskers meows: Meow!
# Bella moos: Moo!

# Polymorphism in action with built-in functions too:
# len() works on strings, lists, and dictionaries — many forms.
print(len("hello"))        # 5
print(len([1, 2, 3]))      # 3
print(len({"a": 1, "b": 2}))  # 2
