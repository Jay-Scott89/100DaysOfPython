# with open(r"C:\Users\Jamie\OneDrive\Documents\Cyber\100DaysOfPython\Intermediate\weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

import csv
with open(r"C:\Users\Jamie\OneDrive\Documents\Cyber\100DaysOfPython\Intermediate\weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas 
data = pandas.read_csv(r"C:\Users\Jamie\OneDrive\Documents\Cyber\100DaysOfPython\Intermediate\weather_data.csv")
print(data)
print(data["temp"])