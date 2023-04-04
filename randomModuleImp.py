import random

num = random.randint(1, 10)

def user_name():
    name = input("Enter your name: ")
    name = name[::-1]
    username = name + str(num)
    return username

print(user_name())
