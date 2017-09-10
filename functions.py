#functions.py
#factorial_recursive
# This function should recursively compute the factorial value of the argument passed in.
# psedocode for factorial:
# Base case if n is 1 
# return n
# else calls itself n*factorial_recursive 
def factorial_recursive(n):
   if n == 1:
       return n
   else:
       return n*factorial_recursive(n-1)

# Change this value for a different result
# input is the num as the argument 
num = int(input("Please Enter a number: "))
# edge cases is to check if num = 0, num < 0
# check is the number is negative
if num == 0:
   print("The factorial of 0 is 1")
elif num < 0:
   print("Sorry, factorial does not exist for negative numbers")
else:
   print("Factorial is", factorial_recursive(num))

