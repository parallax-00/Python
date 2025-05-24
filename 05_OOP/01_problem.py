class Car:
    def __init__(self,brand,model):
       self.brand=brand
       self.model=model
       
my_porsche = Car("Porsche","911")
print(my_porsche.brand)
print(my_porsche.model)

my_merc = Car("Mercedes","AMG Roadster")
print(my_merc.brand)
print(my_merc.model)
