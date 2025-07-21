def generate_password(nr_letters, nr_symbols, nr_numbers):
    import string
    from random import choice, shuffle

    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list(string.punctuation)

    password_list = (
        [choice(letters) for _ in range(nr_letters)] +
        [choice(symbols) for _ in range(nr_symbols)] +
        [choice(numbers) for _ in range(nr_numbers)]
    )
    shuffle(password_list)
    return ''.join(password_list)

def get_user_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

print("Welcome to the PyPassword Generator")
nr_letters = get_user_input("How many letters would you like in your password?\n")
nr_symbols = get_user_input("How many symbols would you like?\n")
nr_numbers = get_user_input("How many numbers would you like?\n")

password = generate_password(nr_letters, nr_symbols, nr_numbers)
print(f"Your password is: {password}")