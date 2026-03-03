from turtle import Turtle

FONT = ("Ariel", 24, "normal")
SCORE_LOCATION = (-280, 265)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        with open(file="data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(SCORE_LOCATION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(SCORE_LOCATION)
        self.write(f"Level: {self.level} High Score: {self.high_score}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def reset(self):
        if self.level > self.high_score:
            self.high_score = self.level
            with open(file="data.txt", mode="w") as file:
                file.write(f"{self.level}")
        self.level = 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="left", font=FONT)