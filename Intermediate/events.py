from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_fwd():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_fwd)
screen.exitonclick()