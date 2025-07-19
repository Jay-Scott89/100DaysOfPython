import os
import random
from game_data import data

def set_game_data():
    return random.choice(data)

def play_game():
    print("Welcome to Higher or Lower")
    game_b = set_game_data()
    score = 0
    is_game_over = False

    while not is_game_over:
        game_a = game_b
        while game_a == game_b:
            game_b = set_game_data()

        print(f"Does {game_a['name']} have a higher or lower Instagram follower count than {game_b['name']}?")
        players_answer = input("Type 'h' or higher or 'l' for lower: ")
        if players_answer == 'h' and game_a['follower_count'] > game_b['follower_count']:
            score += 1
        elif players_answer == 'l' and game_a['follower_count'] < game_b['follower_count']:
            score += 1
        else:
            is_game_over = True
   
    print(f"Your final score was {score}")

while input("Do you want to play a game of Higher or Lower? Type 'y' or 'n': ") == "y":
    os.system('cls')
    play_game()

    