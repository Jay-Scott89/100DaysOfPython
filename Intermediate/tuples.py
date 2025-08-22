import turtle as t
import random

# Tuples cant be changed lke a list. It does not support item assignement. Its imutable 
my_tuple = (1, 3, 8)

timmy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# directions = [0, 90, 180, 270]
# timmy.pensize(15)
timmy.speed("fastest")

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(5)

# for i in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))



screen = t.Screen()
screen.exitonclick()