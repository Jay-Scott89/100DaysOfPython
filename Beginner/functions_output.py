# Function with input
def my_function(something):
    print(something)

my_function(123)

# Function with output
def my_other_function():
    return 3 * 2
output = my_other_function()


# Example of input and output
def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"

name = format_name("jamie", "SCOTT")
print(f"Hello {name}, how are you?")

# 2 Functions with outputs that pass into each other
def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello "))
print(output)

# Multiple returns
def names(first, last):
    if first == "" or last == "":
        print("You did not provide input")
        return
    else:
        print("You did provide input")
        return
    
names("Jamie", "")
