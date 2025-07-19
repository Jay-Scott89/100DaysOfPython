import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' 'm', 'n', 'o','p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Password Generator")
number_of_letters = int(input("How many letters would you like: "))
number_of_numbers = int(input("How many numbers would you like: "))
number_of_special = int(input("How many special characters would you like: "))

total_characters = int(number_of_letters + number_of_numbers + number_of_special)
temp_password = ""

for i in range(0, total_characters):
    if number_of_letters > i:
        temp_password += random.choice(letters)
    if number_of_numbers > i:
        temp_password += random.choice(numbers)
    if number_of_special > i:
        temp_password += random.choice(symbols)

password = ''.join(random.sample(temp_password, len(temp_password)))
print(f"Your password is: {password}")