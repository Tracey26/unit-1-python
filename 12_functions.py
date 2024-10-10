"""
Task 1: Greeting
Write a function that takes a name as a 
parameter and prints a greeting message like "Hello, [name]!".
"""
#Define function and created a parameter
def my_function(name):
    """
    This function will take in any specified name as a parameter and give it a greeting 
    """
    #will print name and given parameter
    print("HELLO" + name)
    #argument is specified
my_function(" Franklin")

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
#defined function and created parameter
def math (square):
    """
    This function will take an integer as a parameter for 'square' and calculate 
    and print the integers' square
    """
    #will return the square of the number
    return square**2
#number is specified for parameter
print(math(15))

"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
#defined function and created parameter for even and odd numbers
def even_or_odd(number):
    """
    This function takes a specified integer as a 'number' and calculates if it
    has a remainder if it does false will print as the number is not even if the 
    number is even true will print
    """
    #will determine if either true or false if the specified number is even or odd
    return str(number % 2 == 0)
#will print true or false of the specified number which is given
print(even_or_odd(35))

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
def rectangle(length, width):
    return length*width
a = rectangle(11,26)
print(f"The area is" + {rectangle})

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""


"""
Task 6: Average of Numbers
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, and returns the total.
Your function should also optionally accept a 3rd argument for discount, and return the discounted if provided.
"""
