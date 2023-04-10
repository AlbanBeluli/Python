class Car():
    def __init__(self, color, use_type):
        self.color = color
        self.use_type = use_type
        self.description = color + " " + use_type

my_car = Car("Red", "Sports Car")

print("Color:", my_car.color)
print("Use Type:", my_car.use_type)
print("Description:", my_car.description)

