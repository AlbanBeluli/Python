class Vehicle():
    def __init__(self, current_speed=0.0):
        self.current_speed = current_speed

    def increrase_speed(self, increment=5.0):
        self.current_speed += increment

class Car(Vehicle):
    def increrase_speed(self, increment=10.0):
        self.current_speed += increment
class Bike(Vehicle):
    def increrase_speed(self, increment=2.0):
        self.current_speed += increment

my_car = Car()
my_bike = Bike()


for i in range(7):
    my_car.increrase_speed()
    my_bike.increrase_speed()

print("Current Car Speed: ", my_car.current_speed)
print("Current Bike Speed: ", my_bike.current_speed)
