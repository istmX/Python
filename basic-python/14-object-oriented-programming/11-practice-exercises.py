# Practice Exercises: OOP
# Each exercise is a small class to build. Solutions are described
# in the comments — try writing the code yourself first!

# ---------------------------------------------------------------
# Exercise 1: Create a Car class
# ---------------------------------------------------------------
# - Attributes: brand, model, year
# - Method: describe() prints "2020 Toyota Corolla"

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def describe(self):
        print(f"{self.year} {self.brand} {self.model}")


my_car = Car("Toyota", "Corolla", 2020)
my_car.describe()   # 2020 Toyota Corolla


# ---------------------------------------------------------------
# Exercise 2: Add a class variable to count objects
# ---------------------------------------------------------------
# - Add a class variable 'total_cars' that increases by 1
#   every time a Car is created.

class CountedCar:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        CountedCar.total_cars = CountedCar.total_cars + 1


CountedCar("Honda")
CountedCar("Suzuki")
CountedCar("Hyundai")
print("Total cars:", CountedCar.total_cars)   # 3


# ---------------------------------------------------------------
# Exercise 3: Inheritance — ElectricCar extends Car
# ---------------------------------------------------------------
# - Add a battery_capacity attribute
# - Add a method charge() that prints "Charging..."

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)   # reuse parent's __init__
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.brand} {self.model} is charging...")


tesla = ElectricCar("Tesla", "Model 3", 2023, 75)
tesla.describe()   # 2023 Tesla Model 3  (inherited method)
tesla.charge()     # Tesla Model 3 is charging...


# ---------------------------------------------------------------
# Exercise 4: Encapsulation — protect the mileage
# ---------------------------------------------------------------
# - Make mileage private (__mileage)
# - Provide drive(kms) to increase it safely
# - Provide get_mileage() to read it

class Bike:
    def __init__(self, brand):
        self.brand = brand
        self.__mileage = 0

    def drive(self, kms):
        if kms > 0:
            self.__mileage = self.__mileage + kms

    def get_mileage(self):
        return self.__mileage


my_bike = Bike("Hero")
my_bike.drive(50)
my_bike.drive(30)
print("Mileage:", my_bike.get_mileage())   # 80
