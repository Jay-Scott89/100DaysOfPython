#Calculator
from art import logo

# Add
def add(n1, n2):
    """Take number one and add it to number two"""
    return n1 + n2

# Subtract
def subtract(n1, n2):
    """Take number one and subtract number two from it"""
    return n1 - n2

# Multiply
def multiply(n1, n2):
    """Take number one and multiply it by number two"""
    return n1 * n2

# Divide
def divide(n1, n2):
    """Take number one and divide it by number two"""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
# User input for a number operator and another number
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        # Conduct the calculation, save the operator and change it to the function then return the answer
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2) 

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()