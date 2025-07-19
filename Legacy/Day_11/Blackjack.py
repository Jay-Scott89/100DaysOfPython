# Blackjack
import random
from art import logo

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players_cards = random.sample(cards, 2)
dealers_cards = random.sample(cards, 2)
end_of_game = False

print(players_cards)
print(f"{dealers_cards[0]}, ?")
player_has_ace = False
dealer_has_ace = False
for card in players_cards:
    if card == 11:
        player_has_ace = True
for card in dealers_cards:
    if card == 11:
        dealer_has_ace = True
players_score = players_cards[0] + players_cards[1]
while not end_of_game:
    player_hit = input("Do you want another card? 'hit' or 'stick' ")
    if player_hit == "hit":
        players_score = players_score + random.choice(cards)
        if player_has_ace and players_score > 21:
            players_score -= 10
        if players_score > 21:
            print(f"Bust. You Loose with a score of: {players_score}")
            end_of_game = True
        print(players_score)
    else:
        dealer_score = dealers_cards[0] + dealers_cards[1]
        while dealer_score < 17:
            dealer_score = dealer_score + random.choice(cards)
        if dealer_has_ace and dealer_score > 21:
            dealer_score -= 10
        if dealer_score > 21:
            print(f"You win! The dealer bust with a score of: {dealer_score}")
            end_of_game = True
        elif players_score > dealer_score:
            print(f"You win! With a score of: {players_score} against the dealers: {dealer_score}")
            end_of_game = True
        elif players_score == dealer_score:
            print(f"Tie! Both you and the dealer got a score of: {dealer_score}")
            end_of_game = True
        else:
            print(f"You loose! The dealer had a score of: {dealer_score} against your: {players_score}")
            end_of_game = True
