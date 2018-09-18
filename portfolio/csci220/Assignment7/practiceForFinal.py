from math import *
from random import randint


def series():
    userN = eval(input("Give me a number: "))

    mySum = 0
    for el in range(1, userN + 1):
        numerator = el + (el+1)
        denominator = 2 ** el
        print(str(numerator) + "/" + str(denominator))
        answer = numerator / denominator
        mySum = mySum + answer

    print(mySum)

def adjustTwo(num):
    num = 100


def genPasswords(inputFileName, outputFileName):
    inPut = open(inputFileName, "r")
    myOutput = open(outputFileName, "a")
    for el in inPut.readlines():
        el = el.split()
        random1 = randint(0,1000)
        random2 = randint(0,1000)
        random3 = randint(0,1000)
        random4 = randint(0,1000)

        if random1 % 2 == 0:
            print(el[0][0].upper(), end='', file= myOutput)
        else:
            print(el[0][0].lower(), end='', file = myOutput)

        if random2 % 2 == 0:
            print(el[1][0].upper(), end='', file = myOutput)
        else:
            print(el[1][0].lower(), end='', file = myOutput)

        if random3 % 2 == 0:
            print(el[0][1].upper(), end='', file = myOutput)
        else:
            print(el[0][1].lower(), end='', file = myOutput)

        if random4 % 2 == 0:
            print(el[1][1].upper(), end='', file = myOutput)
        else:
            print(el[1][1].lower(), end='', file = myOutput)

        print(len(el[1]), file = myOutput)


#genPasswords("textforTesting", 'newFile')

def squareNums():
    userVal = eval(input("Give me a number: "))

    for el in range(userVal):
        for i in range(userVal):
            print(el+1+i, end='')
        print()
squareNums()


