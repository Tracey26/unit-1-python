'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

#Asks user to input a digit
num = int(input("Enter a digit even to or greater than 10: "))
#checks if value of number is equal to or greater than 10
if num >= 10:
    print("true")

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
#prompts user to input their age 
age = int(input("Enter your age: "))
#asks user to verify if they're a student
student = int(input("Press 0 if you are not a student and 1 if you are a student:"))
#checks if age is under 18 and if they are a student
if age < 18 or student == 1:
    print ("Ticket prices are $10")
#if the user is not under 18 or a student "Price is $20 will be printed"
else: 
    print("Price is $20")
    

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
#created fruit list
fruit = ["strawberry","banana","apple","pear"]
#asks user to input a fruit name
name= input("Name a fruit:")

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
