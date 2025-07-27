
hello = "Hello, World"
number = 7

def greet(n):
    print(hello)
    print(n)

greet(number)

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

#Keyword arguments 
greet_with(name="Jimmy", location="UK")
# Positional argumetns
greet_with("Jimmy", "UK")