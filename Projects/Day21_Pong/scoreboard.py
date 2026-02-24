from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.refresh(0, 0)
    
    def refresh(self, player, rival):
        self.clear()
        self.write(f"Player: {player}: Rival: {rival}", align="center", font=("Arial", 16, "normal"))

