import datetime
from random import randint



def bubbleSort(myList):

    timeBefore = datetime.datetime.now()  # this will get the time before sorting
    for outer in range(0, len(myList) - 1): #this loop will run n-1 number of times
        for inner in range(0, len(myList) - 1 - outer): #this loops through 0 to the len(myList) - 1 - outer, this happens because once the outer loop runs once the max value will be at the end and we do not need to compare that once its in its spot and so on and so forth
            if myList[inner] > myList[inner + 1]: #if the current element is greater than the element next to it, they will be swapped
                myList[inner], myList[inner + 1] = myList[inner + 1], myList[inner] #swapping of elements

    timeAfter = datetime.datetime.now()  # this gets the time after sorting
    timeDiff = timeAfter - timeBefore  # this will give the total time sorting

    print("Bubble Sort of size " + str(len(myList)) + " took " + str(timeDiff))

def testIfSorted(myList): #subroutine to test if the list was sorted correctly
    didSwap = False #this variable will change to true if an element was swapped
    for outer in range(0, len(myList) - 1): #this is the same embedded loop as the bubble sort embedded loop
        for inner in range(0, len(myList) - 1 - outer):
            if myList[inner] > myList[inner + 1]:
                myList[inner], myList[inner + 1] = myList[inner + 1], myList[inner]
                didSwap = True
                break

    if didSwap == False: #if no elements were swapped then the list was sorted correctly
        print("The list is sorted!")
    if didSwap == True: #if elemenets were swapped then the list was not sorted correctly
        print("The list was not sorted!")

length = 1000 #beginning length of the list
for el in range(10):
    myList = []

    for list in range(length): #populates the list with 'length' random variables
        myList.append(randint(0,100))

    bubbleSort(myList) #this will call the function to sort the list
    testIfSorted(myList) #this will confirm if the list was sorted correctly

    length = length * 2 #this will double the length for the next list






