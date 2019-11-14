import random

debug = True
context = []

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

def permutations(args):
    '''Module for permutations'''
    print("There are two types of repetition")
    print("Repeition allowed, and no repetition")
    prompt = "(enter 'skip' to go straight to exercise for %s, use flag ' -a' to also skip exercise) "
    print(withReps(input(prompt % "with reptition")))
    print(withNoReps(input(prompt % "without reptition")))

###START MAIN PROGRAM###
applicationName = "Math Reviewer(Title WIP)"
versionNum = "v0.1"
welcomeMessage = "Hello and welcome to the %s %s written by James Ellerbee,\n this application aims to help you review selected math topics" % (applicationName, versionNum)

topics = {
    "Permutations": "A more detailed message about permutations, may inlcude flags the module take",
}

def printAvailableTopics():
    for topic in topics:
        print(topic, end=', ')
    print("\n")

def printWelcome():
    print(welcomeMessage)
    print("the current offered topics are:")
    printAvailableTopics()

def printMenu(args):
    '''outputs the menu options'''
    print("Enter: 'menu' to print menu again.")
    print("'view topics' to print the available topics to visit.")
    print("'help' to print the available list of commands, \ntype 'help <command>' to view more information about a given command.")
    print("'quit' to quit the application.")
    print()

def printHelp(args):
    '''Prints the help information'''
    global mainMenuDict
    global topics
    if len(args) > 1:
        print("unexpected argument!")
        return None
    elif len(args) == 0:
        for key in mainMenuDict:
            print(key +":", mainMenuDict[key][0].__doc__)
    else:
        if args[0] in mainMenuDict:
            print(mainMenuDict[args[0]][1])
            
def programQuit(args): #call to function object
    '''Exits the application'''
    if len(args) > 1:
        print("Invaild number of arguments")
        return None
    ui = ''
    if len(args) == 1:
        if args[0] == 'y':
            ui = "y"
        else:
            print("No such argument '%s'" % args[0])
            return None
    else:
        if ui == "":
            ui = input("are you sure you want to quit? [y/n]")
    if ui != "n":
        print("Goodbye!")
        quit()
    else:
        return None

def printView(args):
    '''Prints the topics in the program'''
    global topics
    if len(args) > 1:
        print("Invaild number of arguments")
    elif len(args) == 1:
        if args[0] == "topics":
            for topic in topics:
                print("%s, " % topic)
        if args[0] == "menu":
            printMenu()
    elif len(args) == 0:
        print("view what?")       

def goBack(args):
    global topicMenuDict
    print("moving back one menu")
    topicMenuDict["back"][2] = True



topicMenuDict = {
    "menu": [printMenu("topic"),
            "print this menu for this sub menu"
            ],
    "back": [goBack, 
            "Use this command to move back to previous menu, there are no available arguments",
            False,
            ],
}

def topicSubMenu(args):
    '''Sub menu for math topics'''
    print("You are now in the topics submenu")
    ui = ''
    while not topicMenuDict["back"][2]:
        ui = input("/main/topic/ > ")
        if ui != "":
            ui = ui.split(" ")
        if ui == "":
            continue
        elif ui[0] in topicMenuDict:
            topicMenuDict[ui[0]][0](ui[1:])
        
        else:
            print("Invaild input, please try again.")

def goToMenu(args):
    '''calls the respected submenu'''
    if args[0] == "topics":
        topicSubMenu(args)

# Expand this dictonary when adding functionality to the program!!!
    #"1": permutations,
    #...
    #"n" : functionForN
mainMenuDict = {
    "view": [printView, 
            "Use this command to view a given argument,\nvaild arguments:\n\t'topics' to display all the topics this application includes\n\t'menu' to view the commands for this menu",
            ],
    "menu": [goToMenu, 
            "Use this command to move to a different menu,\nvaild arguemnts:\n\t'topics' to move to the topics submenu"
            ],
    "help": [printHelp, 
            "You've just used the help command to recursively get help for help.\nUsage: 'help <command>' to view more information about a command"
            ],
    "quit": [programQuit, 
            "Use this command to quit the application,\nvaild arguments:\n\t'y' to auto yes on quit"
            ],
}

def main():
    printWelcome()
    printMenu("")
    ui = ''
    while True:
        ui = input("/main/ > ")
        if ui != "":
            ui = ui.split(' ')
        if ui == "":
            continue
        elif ui[0] in mainMenuDict:
            mainMenuDict[ui[0]][0](ui[1:])
        else:
            print("Invaild input, please try again\n")
main() #call to main 