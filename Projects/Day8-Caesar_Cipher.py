alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, original_text, shift_amount):
    output = ""
    location = 0
    for char in original_text:
        is_upper = False
        if char.isupper():
            is_upper = True
            char = char.lower()
        
        if char in alphabet:
            if direction == 'encode':
                location = alphabet.index(char) + shift_amount
            elif direction == 'decode':
                location = alphabet.index(char) - shift_amount
            location = location % 26
            if is_upper:
                output += alphabet[location].upper()
            else:
                output += alphabet[location]
        else:
            output += char
    print(output)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input ("Type your message: ")
    shift = int(input("Type the shift number: "))

    caesar(direction, text, shift)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no': ").lower()
    if restart == "no":
        should_continue = False
        print("Goodby")
