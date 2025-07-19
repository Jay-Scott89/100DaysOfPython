# Menu list of ingredients that are required for making the coffees
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# What resourse the machine has inside it. This is the maximan that it can hold. 
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Seting of the global variables. 
is_turned_off = False
cash_in_machine = float(0)
money_to_be_paid = float(0)
change = float(0)

# Report function.
def report():
    '''This function does not take any input but is designed to print what ingredients remain within the machine and show how much money if within.'''
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Cash in machine £{cash_in_machine}")
    
# Function for making the Espresso
def make_espresso(water,coffee):
    '''This function takes the global water and coffee in and updates their valuse as they are consumed. It also calls the make payment function and then compaires if enough has been paid.'''
    if water >= MENU['espresso']['ingredients']['water']:
        if coffee >=  MENU['espresso']['ingredients']['coffee']:
            # Get the global variables required and run a function to update multiable variables. 
            global change, cash_in_machine
            change, cash_in_machine = make_payment(change, cash_in_machine)
            if change >= 0:
                # Subtract resouses used from the original totals. 
                resources['water'] = resources['water'] - MENU['espresso']['ingredients']['water']
                resources['coffee'] = resources['coffee'] - MENU['espresso']['ingredients']['coffee']
                print(f"Here is you espresso and your change. £{change}")
            else:
                #If not enough money paid then give back what they had paid. 
                print("Not enough money")
                cash_in_machine -= money_to_be_paid
        else:
            print("Not enough Coffee")
    else:
        print("Not enough water")

# Function for making the latte
def make_latte(water,coffee,milk):
    '''This function takes the global water and coffee in and updates their valuse as they are consumed. It also calls the make payment function and then compaires if enough has been paid.'''
    if milk >= MENU['latte']['ingredients']['milk']:
        if water >= MENU['latte']['ingredients']['water']:
            if coffee >=  MENU['latte']['ingredients']['coffee']:
                global change, cash_in_machine
                change, cash_in_machine = make_payment(change, cash_in_machine)
                if change >= 0:
                    resources['water'] = resources['water'] - MENU['latte']['ingredients']['water']
                    resources['coffee'] = resources['coffee'] - MENU['latte']['ingredients']['coffee']
                    resources['milk'] = resources['milk'] - MENU['latte']['ingredients']['milk']
                    print(f"Here is you latte and your change. £{change}")
                else:
                    print("Not enough money")
                    cash_in_machine -= money_to_be_paid
            else:
                print("Not enough Coffee")
        else:
            print("Not enough water")
    else:
        print("Not enough milk")

# Function for making the cappuccino
def make_cappuccino(water,coffee,milk):
    '''This function takes the global water and coffee in and updates their valuse as they are consumed. It also calls the make payment function and then compaires if enough has been paid.'''
    if water >= MENU['cappuccino']['ingredients']['water']:
        if milk >= MENU['cappuccino']['ingredients']['milk']:
            if coffee >=  MENU['cappuccino']['ingredients']['coffee']:
                global change, cash_in_machine
                change, cash_in_machine = make_payment(change, cash_in_machine)
                if change >= 0:
                    resources['water'] = resources['water'] - MENU['cappuccino']['ingredients']['water']
                    resources['coffee'] = resources['coffee'] - MENU['cappuccino']['ingredients']['coffee']
                    resources['milk'] = resources['milk'] - MENU['cappuccino']['ingredients']['milk']
                    print(f"Here is you cappuccino and your change. £{change}")
                else:
                    print("Not enough money")
                    cash_in_machine -= money_to_be_paid
            else:
                print("Not enough Coffee")
        else:
            print("Not enough milk")
    else:
        print("Not enough water")

# Function for making a payment
def make_payment(change_owed, cash_in_machine):
    '''Takes in and returns the change_owed and cash_in_machine'''
    money = float(input(f"You owe me £{money_to_be_paid}... SO PAY UP! £"))
    change_owed = money - money_to_be_paid
    cash_in_machine += money_to_be_paid
    return change_owed, cash_in_machine

#Start of the program
while not is_turned_off:
    change = 0
    users_choice = input("What do you want? (espresso/latte/cappuccino): ").lower()

    if users_choice == "off":
        is_turned_off = True
        
    elif users_choice == "report":
        report()

    elif users_choice == "espresso":
        money_to_be_paid = MENU['espresso']['cost']
        make_espresso(resources['water'], resources['coffee'])

    elif users_choice == "latte":
        money_to_be_paid = MENU['latte']['cost']
        make_latte(resources['water'], resources['coffee'], resources['milk'])
        
    elif users_choice == "cappuccino": 
        money_to_be_paid = MENU['cappuccino']['cost']
        make_cappuccino(resources['water'], resources['coffee'], resources['milk'])

    else:
        print("I dont know what you want. try again. ")