numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# or through list comprehension you can do this
#new_list = [new_itme for item in list]
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

name = "Jamie"
letter_list = [letter for letter in name]

range_list = [num * 2 for num in range(1,5)]

# Conditional list comprehension
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Claire", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 4]

print(long_names)
#python sequences - list, range, string, tuple

# Squaring numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]
print(squared_numbers)

# Filter Even Numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [n for n in numbers if n % 2 == 0]
print(result)

# Data Overlap
list_1 = [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]
list_2 = [3, 6 ,13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]
result = [int(num) for num in list_1 if num in list_2]
print(result)
