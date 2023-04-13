
# Simple function
def greet():
    print("Hello Alban")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet()

#Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Alban")

# functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Alban", "Munich")


# Functions with key word arguments
def greet_with(name="Alban", location="London"):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with()
