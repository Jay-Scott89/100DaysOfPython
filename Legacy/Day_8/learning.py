# Simple function
def greet():
    print("Hello")
    print("This is my function")
    print("How are you")

greet()

# Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you doing {name}?")

user_name = input("What is your name? ")

greet_with_name(user_name)

# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}? ")

u_name = input("What is your name? ")
u_location = input("Where are you from? ")
greet_with(u_name, u_location)