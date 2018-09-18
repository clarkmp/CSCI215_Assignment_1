from math import *

def checkIfPrime():
    userNumber = eval(input("Give me a number: "))
    if userNumber > 1: #this makes sure the number is greater than 1 which is not a prime number
        while userNumber > 1: #this only loops if the number is greater than 1
            if userNumber % 2 == 0: #this will determine if the number is a prime number or not by seeing if it is a multiple of 2
                print('Your number is not a prime number!')
                break
            else:
                print('Your number is a prime number!')
                break
    else:
        print('Your number is prime!')
checkIfPrime()

def checkIfEven():
    userValue = eval(input('Give me a value: '))
    while userValue > -1: #this runs the loop only if the number is not a negative number
        if userValue % 2 == 0: #if the remainder is 0 then the number is even because it is divisible by 2
            print('The number is even')
        else: #if the remainder is not 0, then it is odd because it is not divisible by 2
            print('The number is odd')
        userValue = eval(input('Give me a value: ')) #since this line is still in the loop it will ask the user for a value again and restarts the loop
#checkIfEven()


def messageEncrypter(list):
    for el in (list): #takes a list and goes through each letter in the list
        if ord(el) > ord('Z'):
            newCharacter = ord(el) - 25
            print(chr(newCharacter), end='')
        elif ord(el) < ord('Z'):
            newCharacter = ord(el) + 25
            print(chr(newCharacter), end='')


firstList = 'M[h[@e^ddo#Yec[#bWj[b_[i$M[b_l[_dj^[Yeic_YXeedZeYai$M[[c[h][Z\hecc_YheX[iWdZckYa$7f[iWh[ekhYeki_di$Ekhj^ek]^jiWdZ\[[b_d]iWh[dej\kbbokdZ[hekhemdYedjheb$J^[h[cWoX[ckY^icWhj[hWdZl[hoZ_\\[h[djX[_d]i[bi[m^[h[$7dZedjefe\Wbbj^_i"m[h[cWa_d]Wc[iie\ekhfbWd[jWdZX[Yec_d]WZWd][hjeekhi[bl[i$'
#secondList = '=djgjbdnonjao`io\gf\]jpooc`"`^jgjbt"ja\ijmb\idnh5oc`o\gg`noj\fdioc`ajm`nodnoc`o\gg`noijoepno]`^\pn`dobm`ramjhoc`c\m_d`no\^jmi6dodnoc`o\gg`no\gnj]`^\pn`ijjoc`mom``n]gj^f`_donnpigdbco'oc`njdg\mjpi_dor\n_``k\i_md^c'ijm\]]do^c`r`_ocmjpbcdon]\mf\n\n\kgdib'\i_ijgph]`me\^f^podo_jri]`ajm`doh\opm`_)'


#messageEncrypter(firstList)

