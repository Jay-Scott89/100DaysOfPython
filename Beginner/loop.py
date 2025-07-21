fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]
# Same Same
print(sum(student_scores))
sum = 0
for score in student_scores:
    sum += score
print(sum)

print(max(student_scores))
max = 0
for score in student_scores:
    if max < score:
        max = score
print(max)

# Range function - does not include the last number! First number is the start, second is the end number(not included), third number is the step number
for number in range(1, 10, 2):
    print(number)
    
total = 0
for number in range(0, 101):
    total += number
print(total)