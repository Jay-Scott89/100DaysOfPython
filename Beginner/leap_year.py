def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    leap_year = False
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                leap_year = True
        else:
            leap_year = True
    return leap_year