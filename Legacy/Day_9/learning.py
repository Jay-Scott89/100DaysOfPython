# Declaring a dictionary
programming_dictionary = {
    "First": "This is the first entry",
    "Second": "This is the second entry",
}

# Printing a specific entry
print(programming_dictionary["Second"])

# Adding to the dictionary
programming_dictionary["Third"] = "This is the third entry"

# Printing the whole dictionary
print(programming_dictionary)

# An empty dicitonary
empty_dictionary = {}

# Edit an item in the dictionary
programming_dictionary["Third"] = "This has now been changed"
print(programming_dictionary["Third"])

# Loop through the dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
# Lists in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting dictionary in a list
travel_logs = [
    {
        "country": "France",
        "Cities_visited": ["Paris", "Lyon"],
        "Total_visits": 12
    },
    {
        "country": "Germany",
        "Cities_visited": ["Berlin", "Munich"],
        "Total_visits": 5
    },
]