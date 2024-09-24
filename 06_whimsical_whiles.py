"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
#defining the counter variable
t = 1
#Establishes that the code will run when t is less than 11
while t < 11:
    #prints the numbers that are less than 11
    print(t)
    #adds 1 the last digit used and will print if less then 11
    t += 1


"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
#defining the counter variable
t = 10
#Establishes that the code will run when t is greater and/or equal to 1
while t >= 1:
    #prints the numbers that are greater and/or equal to 1
    print(t)
    t -= 1


"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
while True:
    #defines counter variables
    r = 1
    fact = 1
    #prompts user to type in a number
    num = int(input("Type a number:"))
    #checks if number is less or equal to 0
    if num <= 0:
        break
    #calculates if it is a factorial
    while r < num:
        r += 1
        fact *= r
    print (fact)

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
#set password
password = "weakpassword"
#prompts user to put in password
guess = input ("Input password")
#checks if input password was correct
while guess != password:
    #prints if password is incorrect
    print("Incorrect password :( ")
    guess = input ("Input password:")
    #printed if password is correct
print("Correct password :)")

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""