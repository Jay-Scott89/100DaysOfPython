from turtle import Turtle

class Paddle:
    def __init__(self):
        self.paddle = Turtle(shape="square")
        self.paddle.penup()
        self.paddle.color("White")
        self.paddle.setheading(90)
        self.paddle.shapesize(stretch_wid=1, stretch_len=6,)

    def players_paddle(self):
        self.paddle.teleport(-550, 0)

    def rival_paddle(self):
        self.paddle.teleport(550, 0)

    def move_up(self):
        if (self.paddle.ycor() < 250):
            self.paddle.forward(50)

    def move_down(self):
        if (self.paddle.ycor() > -250):
            self.paddle.forward(-50)

    def collides_with(self, ball):
        return (abs(self.paddle.xcor() - ball.xcor()) < 20 and
                abs(self.paddle.ycor() - ball.ycor()) < 50)