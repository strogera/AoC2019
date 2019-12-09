def dataOperation(data):
    opDic={"ADD":1, "MULT":2, "IN":3, "OUT":4, "JIT":5, "JIF":6, "LT":7, "EQ":8, "HALT":99 }
    i=0
    while i<len(data):

        instruction=str(data[i])
        op=instruction[-2:]

        instruction=instruction[:-2]
        firstParamMode="0"
        if instruction:
            firstParamMode=instruction[-1]
            instruction=instruction[:-1]
        if (i+1)<len(data):
            if firstParamMode=="0":
                firstParam=data[i+1]
            else:
                firstParam=i+1

        secondParamMode="0"
        if instruction:
            secondParamMode=instruction[-1]
            instruction=instruction[:-1]
        if (i+2)<len(data):
            if secondParamMode=="0":
                secondParam=data[i+2]
            else:
                secondParam=i+2

        thirdParamMode="0"
        if instruction:
            thirdParamMode=instruction[-1]
        if (i+3)<len(data):
            if thirdParamMode=="0":
                thirdParam=data[i+3]
            else:
                thirdParam=i+3

        op=int(op)
        if op==opDic["ADD"]:
            data[thirdParam]=data[firstParam]+data[secondParam]
            i+=4
        elif op==opDic["MULT"]:
            data[thirdParam]=data[firstParam]*data[secondParam]
            i+=4
        elif op==opDic["IN"]:
            x=int(input()) 
            data[firstParam]=x
            i+=2
        elif op==opDic["OUT"]:
            print(data[firstParam])
            i+=2
        elif op==opDic["JIT"]:
            if data[firstParam]!=0:
                i=data[secondParam]
            else:
                i+=3
        elif op==opDic["JIF"]:
            if data[firstParam]==0:
                i=data[secondParam]
            else:
                i+=3
        elif op==opDic["LT"]:
            if data[firstParam]<data[secondParam]:
                data[thirdParam]=1
            else: 
                data[thirdParam]=0
            i+=4
        elif op==opDic["EQ"]:
            if data[firstParam]==data[secondParam]:
                data[thirdParam]=1
            else: 
                data[thirdParam]=0
            i+=4
        elif op==opDic["HALT"]:
            return data
        else:
            return None

def partOne():
    with open("input.txt", "r") as inputFile:
        print("Part One Input:")
        for line in inputFile:
            data=[int(x) for x in line.strip().split(',')]
            data=dataOperation(data)
            if not data:
                print("Input error")


def partTwo():
    with open("input.txt", "r") as inputFile:
        print("Part Two Input:")
        for line in inputFile:
            data=[int(x) for x in line.strip().split(',')]
            data=dataOperation(data)
            if not data:
                print("Input error")



print("Answer for part one: ")
partOne()
print("Answer for part two: ")
partTwo()
