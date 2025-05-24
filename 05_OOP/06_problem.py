class Car:
    total_count=0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.total_count+=1
    def full_name(self):
        return (f"Full name of your Car: {self.brand} {self.model}")
class ElectricCar(Car):
        total_count=0
        def __init__(self, brand, model,battery_size):
             super().__init__(brand, model)
             self.battery_size = battery_size
             ElectricCar.total_count+=1
my_first_car = Car("Mercedes","AMG Roadster")
my_second_car = Car("Jaguar","f-type")
my_EV = ElectricCar("Tesla","Model S","85kWh")

print(my_first_car.brand)
print(Car.total_count)
print(ElectricCar.total_count)

