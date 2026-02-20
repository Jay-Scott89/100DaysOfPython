from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colours[i])
    tim.penup()
    tim.setposition(x=-235, y=y_pos[i])



screen.exitonclick()