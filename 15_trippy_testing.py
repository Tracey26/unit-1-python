"""
Exercise 1: Divide
"""
def divide(a, b):
  """Divides two numbers, handling potential division by zero.

  Args:
    a: The numerator.
    b: The denominator.

  Returns:
    The quotient, or None if b is zero.
  """
#asserts that with integers such as 10 and 2 the division will be calculated
#correctly 
  assert divide(10,2) == 5 
  #asserts that if 0 is input as a dividend then this message will print
  #in order for there not be an error 
  assert b == 0, "Division by zero!"



  if b == 0:
    return None
  else:
    return a / b

"""
Exercise 2: Factorial
"""
def factorial(n):
  """Calculates the factorial of a non-negative integer.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.
  """
  #asserts that the factorials will be calculated correctly as the factorial 
  #of 4 is 24
  assert factorial(4) == 24
  #assers that if 0 is input there will be no hinerance and this will be printed
  assert n == 0, "Cannot calculate factorial of 0"

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

"""
Exercise 3: String Reverse
"""
def reverse_string(string):
  """Reverses a given string.

  Args:
    string: A string to be reversed.

  Returns:
    The reversed string.
  """

  assert reverse_string("hello")

  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string

"""
Exercise 4: Fibonacci
"""
def fibonacci(n):
  """Generates the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """

  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

"""
Exercise 5: Email Validation
"""

import re

def is_valid_email(email):
  """Determines whether email is valid or not

  Args:
    email: The email to validate

  Returns:
    Boolean value if email is valid
  """
  email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+"
  return re.match(email_regex, email) is not None