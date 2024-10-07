"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
#imports the datetime module
from datetime import datetime
#created variable for the current date and time
my_date = datetime.now()
#prints the current date and time
print(my_date)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

#created variable for the current date and time
us_date = datetime.now()
# formatted the date to show up as a U.S standard date 
my_string = us_date.strftime("%m/%d/%Y")
#prints the current date in U.S standard time
print(my_string)


"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
str_1 = "09/09/2007"
str_2 = "07/07/2024"


"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""