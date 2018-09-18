
from math import *
from random import randint

def cowsBulls():

    rand1 = randint(0,9) #these three variables are randomized numbers between 0 and 9
    rand2 = randint(0,9)
    rand3 = randint(0,9)

    for trials in range(0,9):

        userCows = 0 #counter for how many Cows the user gets
        userBulls = 0 #counter for how many Bulls the user gets

        userGuessOne = eval(input("Guess the first random number: "))
        if userGuessOne == rand1:    #this code makes it so that if the user's guess is right then they get one Cow
            userCows = userCows + 1
        elif userGuessOne == rand2:
            userBulls = userBulls + 1  #this code makes it so if the user's guess is right but in the wrong spot they get one Bull
        elif userGuessOne == rand3:
            userBulls = userBulls + 1
        print("You have " + str(userCows) + " cow(s) and " + str(userBulls) + " bull(s)")  #this tells the user how many cows and bulls they have

        userGuessTwo = eval(input("Guess the second random number: "))
        if userGuessTwo == rand2:
            userCows = userCows + 1
        elif userGuessTwo == rand1:
            userBulls = userBulls + 1
        elif userGuessTwo == rand3:
            userBulls = userBulls + 1
        print("You have " + str(userCows) + " cow(s) and " + str(userBulls) + " bull(s)")

        userGuessThree = eval(input("Guess the third random number: "))
        if userGuessThree == rand3:
            userCows = userCows + 1
        elif userGuessThree == rand1:
            userBulls = userBulls + 1
        elif userGuessThree == rand2:
            userBulls = userBulls + 1
        print("You have " + str(userCows) + " cow(s) and " + str(userBulls) + " bull(s)")

        if userGuessOne == rand1 and userGuessTwo == rand2 and userGuessThree == rand3:
            print("You win!")   #this code will tell the user they won if they input all the right answer and end the game
            break
        else:
            print("Game over!") #if they dont win, the code will tell the user Game Over! and restart them unless its their last try

#cowsBulls()

def calcWages():
    userHours = eval(input("How many hours did you work this week? ")) #user input variable for how many hours they work
    userWage = eval(input("What is your hourly pay? ")) #user input variable for how much they make in one hour

    if userHours >= 40: #this will run if the user inputs over 40 hours which is counted as overtime
        overTime = userHours - 40 #this will determine exactly how many hours they worked overtime
        extraWage = userWage + (userWage / 2) #this is how much they earn during overtime
        timeAndHalf = overTime * extraWage #this is the overtime hours multiplied by the overtime wage
        newHours = userHours - overTime #this line will give us the hours that arent overtime
        userPay = newHours * userWage + timeAndHalf #this line takes the normal amount of hours and the normal wage and multiplies them to get their weekly pay plus their overtime pay
    else:
        userPay = userHours * userWage #this line will run only if the user inputs 40 or less hours and calculate pay without overtime

    print("You made " + str(userPay) + " this week!")

#calcWages()





def calcFib():
    userN = eval(input("Give me the number of terms: "))
    firstV= 0
    secondV = 1
    for el in range(userN - 1):
        firstV, secondV = secondV, firstV + secondV  #this line sets 'firstV' equal to 'secondV' and then adds it to the new 'secondV' and repeats 'userN' amount of times
    print(secondV) #prints the final number of the sequence

calcFib()


def rockerPaperSciccors():
    computerWin = 0 #varaible to keep track of the computer's wins
    userWin = 0 #variable to keep track of the user's wins
    for el in range(10):
        randomV = randint(1, 3)  #this is the computer's choice of either rock paper or scissors
        userGuess = eval(input("Input your choice of 1 = Rock, 2 = Paper, 3 = Scissors: ")) #user inputs their choice of either rock, paper, or scissors
        if userGuess == 1 and randomV == 1:
            print("Tie!")                           #
        elif userGuess == 2 and randomV == 2:       #these three 'if' statements determine if the game is a tie
            print("Tie!")                           #
        elif userGuess == 3 and randomV == 3:
            print("Tie!")

        if userGuess == 1 and randomV == 3:
            print("You win!")
            userWin = userWin + 1
        elif userGuess == 2 and randomV == 1:          # these three 'if' statements determine if the user won and keeps track of how many wins the user has
            print("You win!")
            userWin = userWin + 1
        elif userGuess == 3 and randomV == 2:
            print("You win!")
            userWin = userWin + 1

        elif randomV == 1 and userGuess == 3:
            print("You lose!")
            computerWin = computerWin + 1
        elif randomV ==  2 and userGuess == 1:          # these three 'if' statements determine if the computer won and keeps track of how many wins the computer has
            print("You lose!")
            computerWin = computerWin + 1
        elif randomV == 3 and userGuess == 2:
            print("You lose!")
            computerWin = computerWin + 1


    print("You won " + str(userWin) + " time(s)!")
    print("The computer won " + str(computerWin) + " time(s)!")


rockerPaperSciccors()




def series():
    mySum = 0      #accumulator to add up all the terms of the series
    myNumerator = 1
    userN = eval(input("Give me a number: ")) #asks the user for a number to set as how many terms will be added up
    for el in range(userN):
        myNumerator = myNumerator + 3  #this makes the numerator =  4 for the first loop but will continue to add three for the next terms
        currTerm = myNumerator / (3 ** (el+1)) #this line sets the numerator on top and then the denominitor is raised to the power of el+1 to get the powers of 3 as the denominator
        mySum = mySum + currTerm #this accumulates the terms
    print(mySum) #prints the final product



series()




