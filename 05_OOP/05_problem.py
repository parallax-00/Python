class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def fuel_type(self):
        return("Either diesel or petrol")
class ElectriCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
    def fuel_type(self):
        return ("Electric charge")

myCar = Car("Mercedes","AMG Roadster")
myEV= ElectriCar("Tesla","Model S","85kWh")        
print(myCar.brand)
print(myCar.model)
print(myCar.fuel_type())
print(myEV.brand)
print(myEV.model)
print(myEV.fuel_type())