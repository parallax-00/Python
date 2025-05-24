class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    def get_brand(self):
        return self.__brand
    def full_name(self):
        return (f"Full Name of the car is: {self.get_brand()} {self.__model}")
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size= battery_size
my_car = Car("Mercedes","AMG Roadster")        
my_EV = ElectricCar("Tesla","Model S","85kWh")

print(my_car.get_brand())
print(my_car.model)
print(my_EV.get_brand())
print(my_EV.model)
print(my_EV.battery_size)



