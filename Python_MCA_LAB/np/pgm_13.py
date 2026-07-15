class Car:
 def __init__(self, brand, model):
     self.brand = brand
     self.model = model
     print("Constructor called.")
     print("Car Created:", self.brand, self.model)
 def __del__(self):
     print("Destructor called.")
     print("Car object destroyed.")

c1 = Car("BMW", "M3 GTS")
del c1