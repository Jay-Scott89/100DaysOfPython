import random

random_integer = random.randint(1, 10)
#print(random_integer)

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", 
"Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", 
"North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", 
"Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", 
"Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesoda", "Oregon", 
"Kansas", "West Virginia", "Nevada", "Nerbraska", "Colorado", "North Dakota", "South Dakota", 
"Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", 
"Alaska", "Hawaii"]

states_of_america.extend(["Scotland", "jockland"])

print(states_of_america[49])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])


