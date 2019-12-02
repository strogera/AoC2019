def dataOperation(data):
    for i in range(0, len(data), 4):
        if data[i]==1:
            data[data[i+3]]=data[data[i+1]]+data[data[i+2]]
        elif data[i]==2:
            data[data[i+3]]=data[data[i+1]]*data[data[i+2]]
        elif data[i]==99:
            return data
        else:
            return None

def partOne():
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            data=[int(x) for x in line.strip().split(',')]
            data=dataOperation(data)
            if data:
                print(data[0])
            else:
                print("Input error")


def partTwo():
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            data=[int(x) for x in line.strip().split(',')]
            for x in range(100):
                for y in range(100):
                    tempData=list(data)
                    tempData[1]=x
                    tempData[2]=y
                    tempData=dataOperation(tempData)
                    if tempData:
                        if tempData[0]==19690720:
                            print(str(x)+str(y))
                            return
                    else:
                        print("Input error")
            print("Not found")



print("Answer for part one: ")
partOne()
print("Answer for part two: ")
partTwo()
