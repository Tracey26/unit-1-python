'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

#Asks user to input a digit
num = int(input("Enter a digit even to or greater than 10: "))
#checks if value of number is equal to or greater than 10
if num >= 10:
    #is printed if number is equal to 10 or greater
    print("true")
else:
    #is printed if number is NOT equal to 10 or greater
    print("false")

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
#checks if users input is already in the list
if name in fruit:
    print("Yes, that fruit is in the list.")
#will print if the named item is not in the list
else:
    print ("No, that fruit is not in the list.")

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
#prompts user to input a year
year = int(input("Enter a year: "))

#checks if the year is divisble by 100
def century(year):
    return year % 100 == 0

#checks if year is divisble by 4
def leap(year):
    if year % 4 == 0:
        #checks if the year is divisble by 100
        if year % 100 == 0:
            #checks if it is divisble by 100 and if it is it will be divided by 400
            return year % 400 == 0  
        #will print that the year is a leap year if it is divisible by 4 and not 100
        return True  
        #will print if the year is not divisible by 4  
    return False  


def check(year):
    #combines the checks done
    if century(year) and leap(year):
        #prints if the year is a century year and a leap year
        print(f"{year} is a century year and a leap year.")
    else:
        #prints if the year is NOT a century year and a leap year
        print(f"{year} is NOT a century year and a leap year.")
#checks conditions in order to print the right message
check(year)




'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
#asks the user to input the weight and zone of their shipment 
weight = float(input("Input weight in kilograms:"))
zone = input("Enter zone A or B:").upper()


     #calculates the cost based on the entered weight and zone (zone A) 
if zone == 'A':
        cost = weight * 5
     #calculates the cost based on the entered weight and zone (zone B) 
elif zone == 'B':
        cost = weight * 7
    #prints if the order weight is less than 0 kg
else:
        print("Error: Invalid weight")

#prints cost
print(cost)


'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
#asks user to input values for the sides of the triangle
a = float(input("Enter the length of side a:"))
b = float(input("Enter the length of side b:"))
c = float(input("Enter the length of side c:"))


    #tests the triangle inequality theorem
if a + b <= c or a + c <= b or b + c <= a:
        print("Not a triangle: The sum of lengths of any two sides must be greater than length of third side. ")
    #checks what type of triangle it is and prints the type
if a == b == c:
        print("Equilateral triangle")
elif a == b or b == c or a == c:
        print("Isosceles triangle")
else:
        print("Scalene triangle")