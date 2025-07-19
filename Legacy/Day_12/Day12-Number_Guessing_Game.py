import random  

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
lives = 10
target_number = random.randint(1, 100)
is_game_over = False

if difficulty == 'hard':
    lives = 5

while not is_game_over:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == target_number:
        print(f"You got it! The answer was {target_number}")
        is_game_over = True
    elif guess > target_number:
        print("Too high.")
        lives -= 1
    else:
        print("Too low.")
        lives -= 1
    if lives < 1:
        print(f"You've run out of guesses, you lose. The answer was {target_number}.")
        is_game_over = True