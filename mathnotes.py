import random

debug = True

def withRepsExercise():
    nLowerBound = 2
    nUpperBound = 10

    rLowerBound = 1
    rUpperBound = 5

    n = random.randint(nLowerBound, nUpperBound)
    r = random.randint(rLowerBound, rUpperBound)

    print("Exercise: given %d different numbers and I want to choose %d of them, what is the number of permutations?" % (n, r))
    userInput = input("> ")
    while not (userInput.isnumeric() and int(userInput) == n**r):
        errMsg = "unknown error,"
        if not userInput.isnumeric():
            errMsg = "invalid input,"
        elif int(userInput) != n**r:
            errMsg = "your answer is not quite right, remember the formula is n ^ r. where n = %d and r = %d" % (n, r)
        errMsg += " please try again"
        print(errMsg)
        userInput = input("> ")
    print("That is correct, %d ^ %d = %d" %(n, r, n**r))
    print("====================")

def withReps(option):
    '''permutations with repetitions'''
    if option == "skip -a":
        return "skipped"
    if option != "skip":
        print("When repeition is allowed.")
        print("Something has n different types... we have n choices each time")
        input(".")
        print("Example; choosing 3 of n number of things is: n * n * n (n multiplied 3 times)")
        input(".")
        print("More generally; choosing r of something that has n different types")
        input(".")
        print("n * n * ...  r times")
        input(".")
        print("Easiest expressed as exponents: n ^ r")
        input(".")
        print("Example: in combination lock, there are 10 numbers to choose from (0,1,2,3,4,5,6,7,8,9) and we choose 3 of them")

        n = 10
        r = 3
        input(".")
        print("There %d operations ^ %d = %d permutations" % (n, r, n**r))
        input(".")
        print("So the formula is \tn ^ r")
        input(".")
        print("where n is the number of options to choose from")
        input(".")
        print("and we choose r number of those options")
        input(".")
        print("repetion is allowed, order matters")
        input(".")
    withRepsExercise()
    return ""

def withNoRepsExercise():
    return

def withNoReps(option):
    '''permutations with no repetitions'''
    if option == "skip -a":
        return "skipped"
    if option != "skip":
        print("When no repetition is allowed")
        print("In this case we have to reduce the number of available choices each time")
        input(".")
        print("For example; if we can choose from 16 pool balls, what could be the different numbers of ways to pick and order?")
        input(".")
        print("No matter what number ball we pick the first time, on the second pick, we cannot choose the exact ball again")
        input(".")
    return ""

def permutations():
    '''Module for permutations'''
    print("There are two types of repetition")
    print("Repeition allowed, and no repetition")
    prompt = "(enter 'skip' to go straight to exercise for %s, use flag ' -a' to also skip exercise) "
    print(withReps(input(prompt % "with reptition")))
    print(withNoReps(input(prompt % "without reptition")))

###START MAIN PROGRAM###
applicationName = "Math Reviewer(Title WIP)"
versionNum = "v0.1"
welcomeMessage = "Hello and welcome to the %s %s written by James Ellerbee, this application aims to help you review selected math topics" % (applicationName, versionNum)

topics = [
    "Permutations",
    ]

def printAvailableTopics():
    for topic in topics:
        print(topic, end=', ')
    print("\n")

def printWelcome():
    print(welcomeMessage)
    print("the current offered topics are:")
    printAvailableTopics()

def printMenu():
    '''outputs the menu options'''
    print("Enter the number that corresponds to the topic you wish to visit:")
    for i in range(len(topics)):
        print("%d for %s," % (i+1, topics[i]))
    print()
    print("enter 'menu' to print menu again")
    print("enter 'help' to print the available list of commands")
    print("enter 'quit' to quit the application")

def printHelp(args):
    '''Prints the help information'''
    global menuDict
    '''print help menu'''
    for key in menuDict:
        print(key +":", menuDict[key].__doc__)
    input(".")

def programQuit():
    '''Exits the application'''
    print("Goodbye!")
    quit()

# Expand this when adding functionality to the program!!!
menuDict = {
    "1": permutations,
    #...
    #"n" : functionForN
    "help": printHelp,
    "quit": programQuit,
}

def main():
    printWelcome()
    printMenu()
    ui = ''
    while True:
        ui = input("> ")
        if debug:
            if ui != "":
                ui = ui.split(' ')
        if ui in menuDict:
            menuDict[ui]() #call to function object
        elif ui == "":
            continue
        else:
            print("Invaild input, please try again\n")
            input(".")

main() #call to main 