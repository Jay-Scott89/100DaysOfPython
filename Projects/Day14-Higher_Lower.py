from Data.game_data import data
import random 
import os

# Clear the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Get the game data from the data set
def get_game_data():
    game_data = random.choice(data)
    return(game_data)

# Check the players input is valid
def players_answer():
    while True:
        answer = input("Your answer, a or b: ").lower()
        if answer != 'a' and answer !='b':
            print("Type 'a' or 'b' only")
        else:
            return answer

# Check if the playes answer is correct
def is_correct(answer, a_score, b_score):
    if answer == 'a' and  a_score > b_score:
        return True
    elif answer == 'b' and a_score < b_score:
        return True
    else:
        return False

# The main display output 
def display(a_name, b_name):
        print(f"Your current score is {score}")
        print("Who has the most followers on Instagram?")
        print(f"A. {a_name}")
        print("or")
        print(f"B. {b_name}")

# The start of the game
clear()
print("Higher or Lower")
score = 0
game_set_two = get_game_data()

while True:
    # Move the score from B into A and replace B with a new set of data
    game_set_one = game_set_two
    while game_set_one == game_set_two:
        game_set_two = get_game_data()
    
    display(game_set_one['name'], game_set_two['name'])
    answer = players_answer()

    if is_correct(answer, game_set_one['follower_count'], game_set_two['follower_count']):
        score += 1
        clear()
        print("Correct, well done!")
    else:
        clear()
        print(f"That was incorect. Game over, your score was: {score}")
        break
