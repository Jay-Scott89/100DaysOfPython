import pandas

data = pandas.read_csv(r"C:\Users\Jamie\OneDrive\Documents\Cyber\100DaysOfPython\Intermediate\weather_data.csv")

data_dict = data.to_dict()
#print(data_dict)

temp_list = data["temp"].to_list()
average = sum(temp_list) / len(temp_list)
#print(average)
#print(data["temp"].mean())
#print(data["temp"].max())

# Get data in columns
#print(data["condition"])
#print(data.condition)

# Get data in row
#print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
#print(monday.condition)
f = (monday["temp"] * (9/5)) + 32
#print(f)

# Create a dataframe from python
student_data = {
    "students": ["Amy", "James", "Angela"],
    "Scores": [76, 75, 54]
}
data = pandas.DataFrame(student_data)
data.to_csv("new_data.csv")