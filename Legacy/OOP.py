# # Object = Class() naming the class using pascal case.
# #car = CarBlueprint()

# #Turtle lets you create a graphic face and move an object around the screen. 
# from turtle import Turtle, Screen

# # Create the turtle module and call it "timmy", print it to the screen and change its shape and colour.
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("burlywood2")
# # Move timmy forward on the screen
# timmy.fd(100)

# # make the screen apear and have it close when clicked. 
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from re import L
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

