temp_word = ""

for i in range(1, 101):
    if i % 3 == 0:
        temp_word += "Fizz"
    if i % 5 == 0:
        temp_word += "Buzz"
    if(not temp_word):
        print(i)
    else:
        print(temp_word)
        temp_word = ""
    