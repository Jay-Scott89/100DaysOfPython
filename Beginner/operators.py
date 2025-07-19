print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


# If else
if height >= 120:
    print("You can ride the rollercoaser.")
else:
    print("Sorry you have to grow taller before you can ride.")

# 1 "=" is an assingment operator
# 2 "==" is a comparison operator
# However "!=" is a counter comparison
# > is greater than, < lesser than >= greater or equal too...

# % Modulo operator checks the remainder value when conducting a devison 
number = int(input("Number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")