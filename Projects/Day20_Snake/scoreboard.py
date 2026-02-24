from turtle import Turtle

score = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.speed("fastest")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.refresh()
    
    def refresh(self):
        global score
        self.clear()
        self.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))
        score += 1
    
    def game_over(self):
        global score
        score -= 1
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over: {score}", align="center", font=("Arial", 30, "normal"))