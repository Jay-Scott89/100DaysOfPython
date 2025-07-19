print("Hello, World!") #Saying hello, printing text to the terminal
print("Hello\nWorld!") #\n makes a new line within whats being writen

print("Hello, " + input("What is your name? ") + "!") #Concatinate strings 

name = input("What is your name? ")
print("Hello " + name + "!")
length = len(name)
print(length) #longer variable names are separated by _underscores and cant start with numbers


#Subscripting
print("Hello" [0]) # Gets the first one
print("Hello" [-1]) # Gets the last letter