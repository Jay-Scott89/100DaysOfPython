import random

hangman_stages = [
    # Stage 0 - Full hangman
    r"""
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \
    |
    |___
    """,
    # Stage 1
    r"""
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      /
    |
    |___
    """,
    # Stage 2
    r"""
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |
    |
    |___
    """,
    # Stage 3
    r"""
     _______
    |/      |
    |      (_)
    |      \|
    |       |
    |
    |
    |___
    """,
    # Stage 4
    r"""
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |
    |
    |___
    """,
    # Stage 5
    r"""
     _______
    |/      |
    |      (_)
    |
    |
    |
    |
    |___
    """,
    # Stage 6 - Empty gallows
    r"""
     _______
    |/      |
    |
    |
    |
    |
    |
    |___
    """
]

word_list = [
    "apple", "ant", "ball", "bat", "bear", "bird", "book", "boy", "car", "cat",
    "chair", "cheese", "chicken", "cloud", "coat", "cow", "cup", "dance", "desk", "dog",
    "doll", "door", "dragon", "drum", "duck", "egg", "elephant", "fish", "flag", "flower",
    "fox", "frog", "game", "ghost", "girl", "goat", "grape", "hat", "horse", "house",
    "ice", "igloo", "jam", "jelly", "jungle", "kite", "lamp", "leaf", "lion", "man",
    "map", "milk", "monkey", "moon", "mouse", "nest", "nose", "orange", "owl", "panda",
    "pants", "pen", "pencil", "pig", "pizza", "plane", "plant", "queen", "rain", "rat",
    "rice", "ring", "robot", "rock", "roof", "rug", "sand", "school", "shark", "ship",
    "shoe", "snake", "snow", "sock", "spoon", "star", "sun", "table", "tiger", "top",
    "toy", "train", "tree", "truck", "turtle", "watch", "water", "whale", "window", "zebra"
]
blank = "_ "
chosen_word = random.choice(word_list)
lives = 6
for letters in chosen_word:
    print(blank, end="")
print("")

correct_letters = []

while lives > 0:
    
    guess = input("What is your letter? ").lower()
    output = ""
    correct_guess = False
    
    for letter in chosen_word:
        if letter == guess:
            output += letter
            correct_letters.append(guess)
            correct_guess = True
        elif letter in correct_letters:
            output += letter
        else:
            output += blank
    print(output)

    if "_" not in output:
        print("You Win")
        lives = 0
    elif correct_guess == False:
        lives -= 1
        print("You lost a life!")
    print(hangman_stages[lives])
  

print("Game Over")
