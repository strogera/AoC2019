
def partOne():
    with open("input.txt", "r") as inputFile:
        lowerStr, higher = inputFile.read().strip().split('-')
        lower, higher= int(lowerStr), int(higher)
        i=lower
        iStr=lowerStr
        passwords=set()
        while(i<=higher):
            countRepeatingDigit=1
            digitsDecrease=False
            pointer=-1
            for charIndex in range(len(iStr)-1):
                if int(iStr[charIndex])>int(iStr[charIndex+1]):
                        digitsDecrease=True
                        pointer=charIndex
                        break
                elif int(iStr[charIndex])==int(iStr[charIndex+1]):
                        countRepeatingDigit+=1

            if countRepeatingDigit!=1 and not digitsDecrease:
                passwords.add(i)

            if digitsDecrease:
                #if the digits decrease we can ignore some values for i
                #ex: from 156218 we can go to 156666
                iStr=iStr[:pointer]+iStr[pointer]*(len(iStr)-pointer)
                i=int(iStr)
            else:
                i+=1
                iStr=str(i)

        print(len(passwords))


def partTwo():
    with open("input.txt", "r") as inputFile:
        lowerStr, higher = inputFile.read().strip().split('-')
        lower, higher= int(lowerStr), int(higher)
        i=lower
        iStr=lowerStr
        passwords=set()
        while(i<=higher):
            countRepeatingDigit=1
            digitsDecrease=False
            reapeatingDigits=set()
            pointer=-1
            for charIndex in range(len(iStr)-1):
                if int(iStr[charIndex])>int(iStr[charIndex+1]):
                    digitsDecrease=True
                    pointer=charIndex
                    break
                elif int(iStr[charIndex])==int(iStr[charIndex+1]):
                    countRepeatingDigit+=1
                    if charIndex==(len(iStr)-2): #if its at the end of the string
                        reapeatingDigits.add(countRepeatingDigit)
                else:
                    reapeatingDigits.add(countRepeatingDigit)
                    countRepeatingDigit=1

            if 2 in reapeatingDigits and not digitsDecrease:
                passwords.add(i)

            if digitsDecrease:
                #if the digits decrease we can ignore some values for i
                #ex: from 156218 we can go to 156666
                iStr=iStr[:pointer]+iStr[pointer]*(len(iStr)-pointer)
                i=int(iStr)
            else:
                i+=1
                iStr=str(i)

        print(len(passwords))


print("Answer for part one: ")
partOne()
print("Answer for part two: ")
partTwo()
