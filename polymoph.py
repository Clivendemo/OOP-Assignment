class Vehicle:
    def move(self):
        print("The vehicle moves")

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Polymorphic behavior
def travel(vehicle):
    vehicle.move()

# Testing
car = Car()
plane = Plane()
boat = Boat()

travel(car)
travel(plane)
travel(boat)