"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.
"""
#Create float variable
float_var=6.7

#Converted into an integer
int_var=int(float_var)

#Print both float variable and intger
print(str(float_var)+""+str(int_var))


"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""

#Prompts user to input any number
num = float(input("Input a number: "))

#If function was created to check if number is greater than 0 and if it is true, it'll print that it is a positive number.
if num > 0:
    print("It is a positive number")

#If function was created to check if number is 0 and if it is true, it'll print that it is zero.
elif num == 0:
   print("It is zero")

#If the conditions above are not met it will print that it is a negative number.
else:
   print("It is a negative number")


"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
#prompt user to input a float and number
int_var=int(input("Input a integer:"))
float_var=float(input("Input a float:"))

#Prints the answers to the calcultions being done such as addition, subtraction, product, and quotient 
print("sum (addittion): "+str(int_var+float_var))
print("sum (subtraction): "+str(int_var-float_var))
print("product: "+str(int_var*float_var))
print("quotient: "+str(int_var/float_var))

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
#Created dictionary for fruits and their quantities
fruits = {
   'pears': 3,
   'cherries': 6,
   'mangoes': 4,
}
#prints the list of fruit anf their amounts
print(fruits)

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
#create a string
my_string = "2,4,6,8"
#Will print my string
print(my_string)
# will convert the string into a tuple
my_list = my_string.split(",")
print(my_list)