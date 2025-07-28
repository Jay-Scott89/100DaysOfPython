# Nesting is placing dictionary inside dictionarys or lists
my_dictionary = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"], 
    "Germany": ["Stuttgart", "Berlin"], 
}

# Print a specific item from a nested list in a dictioanry
print(travel_log["France"][1])

# Print a specific item from inside a nested list
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# Complex nesting of dictionarys in dictionarys. 
countries = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 8,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Münster"],
        "total_visits": 5
    },
}
# Printing for the nested dics
print(countries["Germany"]["cities_visited"][1])