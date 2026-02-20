from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

turtle.pencolor('black')
turtle.pendown()

def reset():
    turtle.reset()
def walk():
    turtle.forward(10)
def back():
    turtle.back(10)
def left():
    turtle.left(10)
def right():
    turtle.right(10)

while True:
    screen.listen()
    screen.onkey(key="w", fun=walk)
    screen.onkey(key="s", fun=back)
    screen.onkey(key="a", fun=left)
    screen.onkey(key="d", fun=right)
    screen.onkey(key="c", fun=reset)
    screen.exitonclick()
 