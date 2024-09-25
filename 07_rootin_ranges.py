"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
#defines the range of the numbers
for x in range (1,11):
#prints the numbers within that range 
    print(x)

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
#defines the range and by how much to count by
for x in range (900,1001,10):
    #prints the counting of 900 to 1000 by 10
    print(x)

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
#defines the range and by how much to count by
for x in range (1,101,9):
    #prints the counting of 1 to 101 by 9
    print(x)

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""

sum = 0
for i in range (1,11):
    sum += i
print(sum)

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?


- Explain the iterative process that this code executes to get that output
"""

rows = 5
 
for i in range(rows):
     for j in range(i + 1):
         print('*', end=' ')
     print()
