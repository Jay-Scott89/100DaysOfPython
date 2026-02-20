from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up of the screen component
screen = Screen()
screen.setup(width=600, height =600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Bind controls
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# Moving the snake forward
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.refresh()


screen.exitonclick()

# 1. Create a snake body
# 2. Move the snake
# 3. Control the snake
# 4. Detect collison with food
# 5. Create a scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail

