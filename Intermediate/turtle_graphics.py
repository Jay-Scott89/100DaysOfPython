from turtle import Turtle, Screen
import heroes 
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("OrangeRed")

colours = ["CornflowerBlue", "Dark Orchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 270]
timmy.speed("fastest")

for i in range(4):
    timmy.forward(100)
    timmy.left(90)

print(heroes.gen())

timmy.pencolor("Black")
for i in range(10):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

timmy.pendown()
def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)

timmy.pensize(15)

for i in range(200):
    timmy.color(random.choice(colours))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))











screen = Screen()
screen.exitonclick()