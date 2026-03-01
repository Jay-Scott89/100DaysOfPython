from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine
from os import name, system

# Clear the terminal
def clear():
    system('cls' if name == 'nt' else 'clear')

menu = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()
is_On = True

while is_On:
    user_input = input(f"What would you like? ({menu.get_items()}): ").lower()
    clear()
    if user_input == "off":
        is_On = False
    elif user_input == "report":
        cm.report()
        mm.report()
    elif (drink := menu.find_drink(user_input)):
        if cm.is_resource_sufficient(drink):
            if mm.make_payment(drink.cost):
                cm.make_coffee(drink)