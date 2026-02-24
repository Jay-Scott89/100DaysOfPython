from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.penup()
        self.color('white')
        self.shapesize(2, 2)
        self.speed("fastest")
        self.dx = 8        # pixels per frame
        self.dy = 8

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1      # hit top/bottom

    def bounce_x(self):
        self.dx *= -1      # hit a paddle

    def reset(self):
        self.goto(0, 0)
        self.dx *= -1      # send it back toward whoever scored last
