#welcoming the people
print("This is the Calculatinater-inator 9000!!!!")
#prompts user to input two floats
num1 = float(input("Input any number:").strip())
num2 = float(input("Input another number:").strip())
#Lists options for a user to pick a math operation to be performed on given numbers
option = int(input(
    """
    Which math calculation do you want to be performed?:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Floor Division
    6. Exponential
    7. Remainder
    Confirm choice:
    """
))
#checks user's choice and if it is this one this code will be carried out
if option == 1:
    #carries out code and performs addition on user's input itegers
    result1 = num1 + num2
    #prints result of addition
    print(f"The answer is {result1}")
#checks user's choice and if it is this one this code will be carried out
elif option == 2:
    #carries out code and performs subtraction on user's input itegers
    result2 = num1 - num2
    #prints result of subtraction
    print(f"The answer is {result2}")
#checks user's choice and if it is this one this code will be carried out
elif option == 3:
    #carries out code and performs multiplication on user's input itegers
    result3 = num1 * num2
    #prints result of multiplication
    print(f"The answer is {result3}")
#checks user's choice and if it is this one this code will be carried out
elif option == 4:
    #checks if user input 0 as a denominator
    if num2 != 0:
        #carries out code and performs division on user's input itegers
        result4 = num1 / num2
        #prints result of division
        print(f"The answer is {result4}")
    #Will print if user input 0 as denominator
    else:
        print("Cannot calculate with denominator of 0!!!!!")
#checks user's choice and if it is this one this code will be carried out
elif option == 5:
    #carries out code and performs floor division on user's input itegers
    result5 = num1 ** num2
    #prints result of floor division
    print(f"The answer is {result5}")
#checks user's choice and if it is this one this code will be carried out
elif option == 6:
    #carries out code and performs exponential on user's input itegers
    result6 = num1 // num2
    #prints result of exponential
    print(f"The answer is {result6}")
#checks user's choice and if it is this one this code will be carried out
elif option == 7:
    #carries out code and performs remainder on user's input itegers
    result7 = num1 % num2
    #prints result of remainder
    print(f"The answer is {result7}")
else:
    #If the user doesn't pick a valid option this will be printed
    print("Select a VALID operation!!")



