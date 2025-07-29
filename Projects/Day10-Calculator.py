import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply,
    "/": divide,
}

should_continue = True
new_calculation = True

while should_continue:
    clear()
    if new_calculation:
        number_1 = float(input("What is your first number: "))
    else:
        number_1 = output
    operator = input("What operation do you want? + - * / : ")
    number_2 = float(input("What is your second number: "))

    output = operations[operator](number_1, number_2)
    print(output)

    exit = input("Do you want to continue to use the calculator? 'yes' or 'no'")
    if exit != "yes":
        clear()
        break
    
    restart = input(f"Type 'y' to continue calculating with {output}, or 'n' to start a new calcultion: ")
    if restart == "y":
        new_calculation = False
    else:
        new_calculation = True