from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time
from turtle import Screen

# Stop the game
def stop_game():
    global game_is_on
    game_is_on = False
    scoreboard.game_over()

# Set up screen and objects
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

# Controls
screen.listen()
screen.onkey(player.move, "w")
screen.onkey(stop_game, "space")

# Game Loop
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Car behaviour    
    car_manager.create_car()
    car_manager.move_car()

    # Collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            player.reset_position()
            scoreboard.reset()

    # Player reaches finish
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()

# Exit
screen.exitonclick()