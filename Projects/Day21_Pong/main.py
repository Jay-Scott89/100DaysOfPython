from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the Screen
screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("Pong")

# Keep score
player_score = 0
rival_score = 0
scoreboard = Scoreboard()

# Create and move a paddle
player = Paddle()
player.players_paddle()

# Create another paddle
rival = Paddle()
rival.rival_paddle()

screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")
screen.onkey(rival.move_up, "5")
screen.onkey(rival.move_down, "2")

# Create the ball and make it move
ball = Ball()

def reset():
    ball.setpos(0, 0)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    # wall collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # paddle collisions – bounding‑box tests, only when the ball is actually
    # in front of the paddle
    if ball.dx < 0:                     # moving left
        if (ball.xcor() < -540 and
            ball.ycor() < player.paddle.ycor() + 50 and
            ball.ycor() > player.paddle.ycor() - 50):
            ball.bounce_x()
    else:                               # moving right
        if (ball.xcor() > 540 and
            ball.ycor() < rival.paddle.ycor() + 50 and
            ball.ycor() > rival.paddle.ycor() - 50):
            ball.bounce_x()

    # miss detection, scoring
    if ball.xcor() > 590:
        player_score += 1
        scoreboard.refresh(player_score, rival_score)
        reset()

    if ball.xcor() < -590:
        rival_score += 1
        scoreboard.refresh(player_score, rival_score)
        reset()



screen.exitonclick()