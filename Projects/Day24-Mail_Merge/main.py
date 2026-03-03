# TODO: Create a letter using starting_letter.txt
# TODO: For each name in invited_names.txt
# TODO: Replace the [name] placeholder with the actual name.
# TODO: Save the letters in the folder "ReadyToSend"

with open(r"C:\Users\Jamie\OneDrive\Documents\Cyber\100DaysOfPython\Projects\Day24-Mail_Merge\Letters\starting_letter.txt") as file:
    starting_letter = file.read()

with open(r"C:\Users\Jamie\OneDrive\Documents\Cyber\100DaysOfPython\Projects\Day24-Mail_Merge\Names\invited_names.txt") as file:
    names = file.readlines()

output_folder = r"C:\Users\Jamie\OneDrive\Documents\Cyber\100DaysOfPython\Projects\Day24-Mail_Merge\Output\Ready_to_send"

for name in names:
    clean_name = name.strip()
    letter = starting_letter.replace("[name]", clean_name)

    file_name = clean_name.replace(" ", "_")
    output_path = fr"{output_folder}\letter_for_{file_name}.txt"
    with open(output_path, "w") as file:
        file.write(letter)

# Hint1: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: https://www.w3schools.com/python/ref_string_strip.asp

# Absolute file path
# C:\Users\Jamie\OneDrive\Documents\Cyber\100DaysOfPython\Projects\Day24-Mail_Merge
