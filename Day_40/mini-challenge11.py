"""🎯 Task
- Create a base class called Vehicle with:
- Attributes: brand, year
- Method: display_info() that prints brand and year
- Create two child classes:
- Car → adds num_doors attribute and a method car_type() that prints "This car has X doors"
- Bike → adds engine_cc attribute and a method bike_type() that prints "This bike has a Xcc engine"
- Create one object of each class and call all relevant methods.
"""
class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"\nBrand:{self.brand}  Year:{self.year}")

class Car(Vehicle):
    num_doors = 4

    def car_type(self):
        print(f"This car has {self.num_doors} doors\n")

class Bike(Vehicle):
    engine_cc = 150

    def bike_type(self):
        print(f"This bike has a {self.engine_cc}cc engine")


car = Car("Honda",2022)
car.display_info()
car.car_type()
bike = Bike("Yamaha",2025)
bike.display_info()
bike.bike_type()