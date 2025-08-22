# import colorgram
import turtle as turtle_module
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(134, 166, 201), (219, 150, 110), (198, 135, 146), (32, 42, 59), (166, 58, 48), (44, 105, 151), (141, 183, 162), (236, 211, 95), (145, 62, 68), (213, 84, 73), (35, 60, 54), (53, 111, 91), (158, 32, 30), (168, 30, 33), (232, 169, 160), (228, 162, 167), (16, 98, 70), (169, 188, 221), (57, 53, 50), (53, 44, 49), (182, 104, 112), (30, 60, 111), (110, 127, 157), (175, 199, 188), (35, 150, 207), (63, 65, 57)]

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

# Move timmy to the start position
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()