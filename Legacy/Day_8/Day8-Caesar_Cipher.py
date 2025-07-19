alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c',
 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 
 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)

def caesar(start_text, shift_amount, shift_dirction):
    end_text = ""
    for letter in start_text:
        if (letter.isalpha()):
            position = alphabet.index(letter)
            if shift_dirction == "encode":
                new_position = position + shift_amount
            elif shift_dirction == "decode":
                new_position = position - shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {shift_dirction}d text is {end_text}")

should_continue = True
while should_continue:
    dirction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26

    caesar(start_text=text, shift_amount=shift, shift_dirction=dirction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")