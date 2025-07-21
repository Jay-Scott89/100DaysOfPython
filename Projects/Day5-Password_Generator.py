import string
from random import choice
from random import shuffle

letters = list(string.ascii_letters)  # ['a', 'b', ..., 'A', 'B', ...]
numbers = list(string.digits)  # ['0', '1', ..., '9']
symbols = list("!@#$%&*?")  

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password\n"))
nr_symbols = int(input("How many symbold would you like?\n"))
nr_number = int(input("How many numbers would you like?\n"))
total = nr_letters + nr_number + nr_symbols
password_list = []

for char in range(0, nr_letters):
    password_list.append(choice(letters))
for char in range(0, nr_symbols):
    password_list.append(choice(symbols))
for char in range(0, nr_number):
    password_list.append(choice(numbers))


shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
