size_price = [15, 20, 25] # Prices are S, M, L
pepperoni_price = [2, 3] # Price is based on S pizza or M&L pizza
extra_cheese_price = 1 # Price is irespective of size
bill = 0

print("Welcome to Python Pizza!")
size = input("What size pizza do you want? S, M, L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    bill += size_price[0]
elif size == "M":
    bill += size_price[1]
elif size == "L":
    bill += size_price[2]
else:
    print("Sorry I did not understand")

if pepperoni == "Y":
    if size == "S":
        bill += pepperoni_price[0]
    else:
        bill += pepperoni_price[1]

if extra_cheese == "Y":
    bill += extra_cheese_price

print(f"Your total bill is £{bill}.")