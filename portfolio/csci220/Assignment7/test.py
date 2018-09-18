


myList = [4,3, 2, 1]



for outer in range(0, len(myList) - 1):
    for inner in range(0, len(myList) - 1 - outer):
        if myList[inner] > myList[inner + 1]:
            myList[inner], myList[inner + 1] = myList[inner + 1], myList[inner]

print(myList)


didSwap = False
for outer in range(0, len(myList) - 1):
    for inner in range(0, len(myList) - 1 - outer):
        if myList[inner] > myList[inner + 1]:
            myList[inner], myList[inner + 1] = myList[inner + 1], myList[inner]
            didSwap = True

if didSwap == False:
    print("The list is sorted!")