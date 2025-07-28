import os # Required to be able to clear the terminal

# Clear the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

bids = {}
should_continue = True
clear()
print("Welcome to the Silent Auction")

# Forces the program to loop while bids are still being submitted
while should_continue:
    
    bidder = input("What is your name?: ")
    bid = int(input("what is your bid?: £"))
    bids[bidder] = bid

    restart = input("Any more bidders? 'yes' or 'no': ")
    clear()
    if restart != "yes":
        should_continue = False

# Get the name (key) with the highest value
winner_bidder = max(bids, key=bids.get)
winning_bid = bids[winner_bidder]

print(f"The winning bid is by {winner_bidder}, with a bid of £{winning_bid}.")