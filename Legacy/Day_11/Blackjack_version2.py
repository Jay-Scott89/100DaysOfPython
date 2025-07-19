import random

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(card_set):
    score = sum(card_set)
    if score == 21:
        return 0
    return score

players_cards = []
dealers_cards = []

for _ in range (2):
    players_cards.append(deal_cards())
    dealers_cards.append(deal_cards())

player_score = calculate_score(players_cards)
dealer_score = calculate_score(dealers_cards)