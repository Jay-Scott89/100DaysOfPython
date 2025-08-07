import os

MENU = {
    "espresso": {
        "ingredients":{
            "water": 50, 
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients":{
            "water": 200, 
            "milk": 150, 
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients":{
            "water": 250, 
            "milk": 100, 
            "coffee": 24
        },
        "cost": 3.0
    }
}

# Clear the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def update_resources(water, milk, coffee):
    global resources
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee
    return 

def refill_machine():
    global resources
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    print_report()
    return

def print_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {resources['money']}")
    return

def has_enough_resources(drink_name, resources):
    for item, required_amount in MENU[drink_name]["ingredients"].items():
        if resources.get(item, 0) < required_amount:
            print(f"Not enough {item}.")
            return False
    return True

def take_payment(price):
    while True:
        try:
            global resources
            payment = 0
            payment += int(input("How many quarters: ")) * 0.25
            payment += int(input("How many dimes: ")) * 0.1
            payment += int(input("How many nickles: ")) * 0.05
            payment += int(input("How many pennies: ")) * 0.01
            print(f"You have payed ${payment:.2f}")
            if payment == price:
                print("Exact ammount provided. No change required.")
                resources["money"] += price
                return True
            elif payment > price:
                change = payment - price
                print(f"Your change is ${change:.2f}")
                resources["money"] += price
                return True
            else:
                return False
        except ValueError:
            print("Whole numbers only!")

def make_drink(used_ingredients):
    global resources
    for item in used_ingredients:
        resources[item] -= used_ingredients[item]

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0
}

clear()

is_on = True
while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
    clear()
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        print_report()
    elif user_input in MENU:
        if has_enough_resources(user_input, resources):
            drink_price = MENU[user_input]["cost"]
            print(f"Your {user_input} will cost ${drink_price:.2f}")
            if take_payment(drink_price):
                make_drink(MENU[user_input]["ingredients"])
                print(f"Enjoy your {user_input}. Enjoy!")
            else:
                print("Sorry that's not enough money. Cash refunded.")
        else:
            print("Please restock the machine.")
    elif user_input == "restock":
        refill_machine()
        print("The machine has been restocked.")
print("Thank you for using the coffee machine")