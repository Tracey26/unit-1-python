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
userin = (input("Type something: ")).strip()

#Checks to see if user input a valid response
if userin.strip() == "":
    print("Invalid Input")
else:
    print("Valid Input")



"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
#Asks for user input on which is better dogs or cats
dogsrbetter = (input("Type in which is better a dog or cat?: ")).strip().lower()

#Will replace the word cat to dog
saydog = dogsrbetter.replace("cat","dog")

#will print the replaced answer which will be dog
print(saydog)


"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""

#Asks user to input age
age = (input("How old are you?: "))
#Asks user to input name
name = (input("What is your name?: "))

#Prints the name of the user as well as the name
print(f"{name} is {age} years old")



"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
#asks for user input of two floats
onefloat = float(input("Input a float: ").strip())
twofloat = float(input("Input another float: ").strip())


#Divides the two floats
quo = onefloat/twofloat

#rounds the quotient to the nearest tenth
quo = f"Answer: {quo:.2f}"

#prints the rounded answer
print(quo)