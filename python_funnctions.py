import sys, random, re
# Solution to problem 10; fibonacci
def iter_fib(num):
    # Keeps track of the number, what number to add next,
    # and specifically a temporary holder for switching things up
    # fibonacci is tricky because you don't want to overwrite
    currentNum = 1
    prevNum = 0
    temp = 0

    # how do defaults even work \o/
    if num == None:
        num = 10

    # basic loop for fibonacci. As an example, let's say we're at 1 2 3 5
    # take whatever number is up, add the previous number. (5+3, next num is 8)
    # temp holds the previous number to add to the new number (temp = 3)
    # load up the new previous number (the new prevnum is now 5)
    # now load up the new current number (we're moving onto 3+5 or 8)
    for i in range(num):
        print currentNum+prevNum
        temp = prevNum
        prevNum = currentNum
        currentNum = temp+currentNum


def mostcommon(k):
    # LIST LIST LIST LIST list
    # I need all of these for reasons
    teststring = "egg cake fish egg cake chicken cake James mother father chicken egg"
    dictionary = teststring.split()
    alreadyplaced = []
    currentlist = []
    currentWord = None

    for i in range(len(dictionary)):
        # make it lower case first for ease, also non-alphanum disappear
        dictionary[i] = filter(str.isalnum, dictionary[i].lower())

        if dictionary[i] in alreadyplaced:
            # I feel like there's a better way to use this but tuples messed me up
            # The index in alreadyplaced will always be the same in currentlist
            currentWord = alreadyplaced.index(dictionary[i])
            currentlist[currentWord] = [currentlist[currentWord][0]+1, currentlist[currentWord][1]]
        else:
            #1st instance to initialize
            currentlist.append([1, dictionary[i]])
            alreadyplaced.append(dictionary[i])

    # Sort the list
    currentlist = sorted(currentlist, reverse=True)
    # Print the list depending on k
    for j in range(k):
            print sorted(currentlist[j])



if __name__ == "__main__":
    # How many times you wanna run fibonacci
    fibs = 5
    if len(sys.argv) == 2:
        fibs = int(sys.argv[1])
    print "Running fibonacci", fibs, "times:"
    iter_fib(fibs)
    dice_roll()
    mostcommon(3)

