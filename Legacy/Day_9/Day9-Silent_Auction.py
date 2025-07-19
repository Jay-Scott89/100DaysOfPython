import os
from art import logo
print(logo)

enterd_bids = {}
bidding_complete = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of £{highest_bid}")

while not bidding_complete:
    bidder_name = input("What is your name? ")
    bid = int(input("What is your bid? £"))
    enterd_bids[bidder_name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' ")
    if should_continue == "no":
        bidding_complete = True
        find_highest_bidder(enterd_bids)
    else:
        os.system('cls')
