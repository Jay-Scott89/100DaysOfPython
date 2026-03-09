# new_dict ={new_key:new_value for item in list}
# new_dict ={new_key:new_value for (key, value) in dict.items()}
# new_dict ={new_key:new_value for (key, value) in dict.items() if test}

import random

names = ["Alex", "Beth", "Claire", "Dave", "Eleanor", "Freddie"]
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score > 60}
print(passed_students)

# Dictionary Comprehension 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}

# Dictionary Comprehension 2
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)