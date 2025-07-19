import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
display = []
chosen_word = random.choice(word_list)
end_of_game = False
lives = 6

for _ in range(len(chosen_word)):
    display += '_'

while not end_of_game: 
    guess = input("Choose a letter to guess: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}.")

    print (f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")
    
    print(stages[lives])