from turtle import Turtle
import random

GAME_BOUNDRY = [-270, 270]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(GAME_BOUNDRY[0], GAME_BOUNDRY[1])
        random_y = random.randint(GAME_BOUNDRY[0], GAME_BOUNDRY[1])
        
        self.goto(random_x, random_y)