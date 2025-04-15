# activity2.py

# Base Class
class Vehicle:
    def move(self):
        pass  # This will be overridden by subclasses

# Car Class
class Car(Vehicle):
    def move(self):
        print("Driving")

# Plane Class
class Plane(Vehicle):
    def move(self):
        print("Flying")

# Example Usage
if __name__ == "__main__":
    print("=== Activity 2: Polymorphism ===")
    car = Car()
    plane = Plane()

    # Polymorphism in action
    vehicles = [car, plane]
    for vehicle in vehicles:
        vehicle.move()
