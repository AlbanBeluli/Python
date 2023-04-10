class Car():
    def __init__(self, color, use_type):
        self.color = color
        self.use_type = use_type

    @property
    def description(self):
        return self.color + " " + self.use_type
    
    @description.setter
    def description(self, desc):
        color, use_type = desc.split(" ")
        self.color = color
        self.use_type = use_type


my_car = Car("Blue", "Sports Car")
my_car.description = "Blue Van"

print("Color:", my_car.color)
print("Use Type:", my_car.use_type)
print("Description:", my_car.description)
