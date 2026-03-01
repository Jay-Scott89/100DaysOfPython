from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time
from turtle import Screen

# Set up screen and objects
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Detect players movement
screen.listen()
screen.onkey(player.move, "w")

# Set game variables
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Spawn cars and move them across the screen    
    car_manager.create_car()
    car_manager.move_car()

    # Detect impact with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # Detect if the player makes it to the other side
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()

scoreboard.game_over()
screen.exitonclick()

#TODO change speeds
#TODO Show levels
#TODO Game over screen