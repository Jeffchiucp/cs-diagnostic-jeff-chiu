
#fizzbuzz.py #Write an algorithm (in English) here's my algorithm, takes two inputs, start and end that prints every number from start to end (inclusive). #However, if a number is evenly divisible by 3, #print the word “fizz” instead of the number #If a number is evenly divisible by 5, #print “buzz” instead of the number. # My algorithm for fizzbuzz # Input: Start and End Number #start and end that prints every number from start to end (inclusive).

#fizzbuzz.py
# Use for loop and if statement to checks the following 3 conditions
fizzbuzz = []

start = int(input("Start Value:"))
end = int(input("End Value:"))

def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)

# apply all the value to all o the range from start to the end
for x in map(fizzbuzz, range(start,end+1)):
    print x
