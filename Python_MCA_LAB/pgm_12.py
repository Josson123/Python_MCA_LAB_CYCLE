class Vehicle:
    def __init__(self, maxSpeed, mileage):
        self.maxSpeed = maxSpeed
        self.mileage = mileage
car = Vehicle(180, 20)

print("Maximum Speed:", car.maxSpeed,"km/h")
print("Mileage:", car.mileage,"kmpl")