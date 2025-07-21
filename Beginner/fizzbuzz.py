for number in range (1, 101):
    print_out = ""
    if number % 3 == 0:
        print_out += "Fizz"
    if number % 5 == 0:
        print_out +="Buzz"
    if print_out == "":
        print(number)
    else:
        print(print_out)