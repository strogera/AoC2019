import math

def partOne():
    sum=0
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            sum+=math.floor(int(line)/3)-2
    print(sum)


def partTwo():
    sum=0
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            fuel=math.floor(int(line)/3)-2
            tempFuel=fuel
            while True:
                tempFuel=math.floor(tempFuel/3)-2
                if tempFuel>0:
                        fuel+=tempFuel
                else:
                    break
            sum+=fuel
    print(sum)


print("Answer for part one: ")
partOne()
print("Answer for part two: ")
partTwo()
