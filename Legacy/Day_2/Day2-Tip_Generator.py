#Each person should pay (150.00 / 5) * 1.12
print("Welcome to the tip calculator")
bill_total = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
number_of_persons = int(input("How many people to split the bill? "))

dec_tip_percentage = tip_percentage / 100 #Divide the tip to a percentage
percentage_to_be_added = dec_tip_percentage * bill_total # multiply the tip by the bill
bill_total = bill_total + percentage_to_be_added #Add the percentage to the bill
total_to_pay = (bill_total / number_of_persons) #Divide the bill amonge those who are paying
total_to_pay = round(total_to_pay, 2) #Round the total to 2 decimal places
total_to_pay = "{:.2f}".format(total_to_pay) #Have the output formated to 2 places
print(f"Each person should pay: ${total_to_pay}") #Print the results