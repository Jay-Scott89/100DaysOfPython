import os
import random 

# Clear the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Get the dificulty of game from the user
def difficulty():
    while True:
        tries = ""
        choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if choice == 'easy':
            tries = 10
            return tries
        elif choice == 'hard':
            tries = 5
            return tries
        else:
            print("Invalid input. Type 'easy' or 'hard'")

def players_input():
    while True:
        try:
            num = int(input("Make a guess: "))
            if num >= 1 and num <= 100:
                return num
            elif num > 100:
                print("Too high, keep guesses between 1 and 100")
            elif num < 1:
                print("Too low, keep guesses between 1 and 100")
        except ValueError:
            print("Whole numbers only!")

def winner(tries_remaining):
    clear()
    print(f"Congradulations, you beat the computer with {tries_remaining} tries remaining!")

def looser(computer_number):
    print(f"You are out of guesses the computers number was {computer_number}")

# Start of the game
clear()
print("Welcome")
players_remaining_tries = difficulty()
computer_number = random.randint (1, 100)

while True:
    print(f"You have {players_remaining_tries} attempts remaing to guess the number.")
    guess = players_input()
    if guess == computer_number:
        winner(players_remaining_tries)
        break
    elif guess > computer_number:
        print("Too high")
    else:
        print("Too low")

    players_remaining_tries -= 1
    if players_remaining_tries < 1:
        looser(computer_number)
        break
    print("Guess again")
    
