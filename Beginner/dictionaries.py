# They work like a table with a key in colum 1 and a value in colum 2. 
#{key: Value}
colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow",
}
print(colours["apple"])

# Add to the dictionary
colours["peach"] = "pink"

# Edit an existing value
colours["apple"] = "green"

# Loop through and print keys or values in a dictionary
for key in colours:
    print(key)
    print(colours[key])

# Wipe a dictionary - Could be used in a fualt or restart 
colours = {}