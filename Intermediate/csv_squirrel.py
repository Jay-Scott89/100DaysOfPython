#TODO Count how many grey, red, black squirls and make a new CSV. 
import pandas
data = pandas.read_csv(r"C:\Users\Jamie\OneDrive\Documents\Cyber\100DaysOfPython\Intermediate\2018_Squirrel_Data.csv")

colors = data["Primary Fur Color"]

black = colors.str.count("Black")
grey = colors.str.count("Gray")
red = colors.str.count("Cinnamon")

squirrel_data = {
    "Colours": ["Black", "Gray", "Red"],
    "Total": [black.sum(), grey.sum(), red.sum()]
}

data_series = pandas.DataFrame(squirrel_data)
data_series.to_csv("Squirl_Count.csv")

#print(black.sum())
#print(grey.sum())
#print(red.sum())

# 