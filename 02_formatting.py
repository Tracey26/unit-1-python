"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""

#Prompt user to input a password
attempt = (input("Enter Password:")).lower()

#Actual password
password="steam123"

#Checks that the password is correct
if attempt == password:
    print("Password correct")
else:
    print("Incorrect Password")


"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
#Asking the user for input
userin = (input("User input: ")).strip()

#Checks to see if user input a valid response
if userin.strip() == "":
    print("InValid Input")
else:
    print("Valid Input")



"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
#Asks for user input on which is better dogs or cats
dogsrbetter = (input("Type in which is better dogs or cats?: ")).strip().lower()








"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""


"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""