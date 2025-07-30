import os
import random

cards = {
    "Ace": 11, 
    "2": 2, 
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
}

# Clear the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# return a card from the cards dict
def deal_card():
    card, value = random.choice(list(cards.items()))
    return {card: value}

# Calculate the hand
def scores(hand):
    return sum(hand.values())

# Join the values from the dict keys to show output
def display_hand(hand):
    return ', '.join(hand.keys())

# Keep looping until the plater stands or busts
def player_turn(players_hand):
    while True:
        print(f"Your hand: {display_hand(players_hand)} | Score: {scores(players_hand)}")
        if scores(players_hand) > 21:
            print("Bust! You went over 21.")
            return False
        choice = input("Hit or Stand? ").lower()
        if choice == 'hit':
            players_hand.update(deal_card())
        elif choice == 'stand':
            return True
        else:
            print("Invalid input. Type 'hit' or 'stand'.")

# Keep giving the computer cards until they have 17 or higher
def computer_turn(computers_hand):
    while scores(computers_hand) < 17:
        computers_hand.update(deal_card())

def play_game():
    players_hand = {}
    computers_hand = {}

    for _ in range(2):
        players_hand.update(deal_card())
        computers_hand.update(deal_card())

    print(f"Computer is showing: {list(computers_hand.keys())[0]}")
    print()

    player_alive = player_turn(players_hand)
    if not player_alive:
        return scores(players_hand), scores(computers_hand)

    computer_turn(computers_hand)

    return scores(players_hand), scores(computers_hand)

# Game loop
while True:
    clear()
    print("Welcome to Blackjack")
    
    player_score, computer_score = play_game()

    print("Final Results:")
    print(f"Your score: {player_score}")
    print(f"Computer's score: {computer_score}")

    if player_score > 21:
        print("You lose! (Busted)")
    elif computer_score > 21:
        print("Computer busted. You win!")
    elif player_score > computer_score:
        print("You win!")
    elif player_score == computer_score:
        print("It's a tie.")
    else:
        print("You lose.")

    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        break
