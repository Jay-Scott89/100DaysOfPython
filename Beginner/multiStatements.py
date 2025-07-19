print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
prices = [5,7,12,0] # Prices are set to Child, Teenager, Adult, special age
bill = 0

if height >= 120:
    print("You can ride the rollercoaser.")

    age = int(input("What's your age? "))
    if age <= 12:
        bill += prices[0]
        print(f"A childs ticket is £{prices[0]}.")
    elif age <= 18:
        bill += prices[1]
        print(f"A Teenager ticket is £{prices[1]}.")
    elif age >= 45 and age <= 55:
        bill += prices[3]
        print("Your ride is free!")
    
    else:
        bill += prices[2]
        print(f"An adult ticket is £{prices[2]}")

    wants_photo = input("Do you want to have a photo? Type y for Yes and n for No. ")
    if wants_photo == "y":
        bill += 3
    print(f"Your final bill is £{bill}.")
else:
    print("Sorry you have to grow taller before you can ride.")