# Instance, Class, and Static Methods
# Three kinds of methods you can define in a class.

class MathUtils:
    # Class variable
    school_name = "ISTMX School"

    def __init__(self, owner):
        self.owner = owner      # instance variable

    # 1. Instance method: works with one object's data
    #    Always takes 'self' as the first parameter.
    def show_owner(self):
        print(f"Owner: {self.owner}")

    # 2. Class method: works with the class itself
    #    Takes 'cls' (the class) as the first parameter.
    @classmethod
    def show_school(cls):
        print(f"School: {cls.school_name}")

    # 3. Static method: belongs to the class but uses NO object
    #    or class data. Like a normal function that lives inside
    #    the class for organization.
    @staticmethod
    def add(a, b):
        return a + b


# Instance method: call it on an object
utils = MathUtils("Aryan")
utils.show_owner()          # Owner: Aryan

# Class method: call it on the class (or an object)
MathUtils.show_school()     # School: ISTMX School
utils.show_school()         # School: ISTMX School (also works)

# Static method: call it on the class (or an object)
print(MathUtils.add(3, 5))  # 8
print(utils.add(10, 20))    # 30 (also works)

# When to use which:
# - instance method  -> you need the object's data (self)
# - class method     -> you need class-level data (cls)
# - static method    -> you need neither, just a related function
