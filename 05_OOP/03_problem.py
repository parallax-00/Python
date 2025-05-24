class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return (f"Full name of the car: {self.brand} {self.model}")

my_car = Car("Mercedes","AMG Roadster")
print(my_car.brand)
print(my_car.model)

class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_EV = Electric_car("Tesla","Model S","90kWh")
print(my_EV.brand)
print(my_EV.model)
print(my_EV.battery_size)
