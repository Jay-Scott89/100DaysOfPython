# Open a file and read from it
with open(file="my_file.txt") as file:
    contents = file.read()
    print(contents)

# How to write to a file. If file does not exist then a new file will be created, but only when in "r" mode
with open(file="my_file.txt", mode="a") as file:
    file.write("\nHello")

# This is a way to open the file, but above is better
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()