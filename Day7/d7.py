def dataOperation(data, inputVals):
    opDic={"ADD":1, "MULT":2, "IN":3, "OUT":4, "JIT":5, "JIF":6, "LT":7, "EQ":8, "HALT":99 }
    i=0
    inputIndex=0
    outPut=-1
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
            thirdParaModem=instruction[-1]
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
            data[firstParam]=inputVals[inputIndex]
            inputIndex+=1
            i+=2
        elif op==opDic["OUT"]:
            outPut=data[firstParam]
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
            return (data, outPut)
        else:
            return None

def partOne():
    with open("input.txt", "r") as inputFile:
        for line in inputFile:
            data=[int(x) for x in line.strip().split(',')]
            output=[]
            out=-1
            phase=[]
            for a in range(5):
                output2=[]
                dataC=list(data)
                (dataC,out)=dataOperation(dataC, [a, 0])
                phase=[a]
                if out==-1:
                    continue
                for b in range(5):
                    if b in phase:
                        continue
                    phase.append(b)
                    (dataC2,out2)=dataOperation(dataC, [b, out])
                    if out2==-1:
                        continue
                    for c in range(5):
                        if c in phase:
                            continue
                        phase.append(c)
                        (dataC3,out3)=dataOperation(dataC2, [c, out2])
                        if out3==-1:
                            continue
                        for d in range(5):
                            if d in phase:
                                continue
                            phase.append(d)
                            (dataC4,out4)=dataOperation(dataC3, [d, out3])
                            if out4==-1:
                                continue
                            for e in range(5):
                                if e in phase:
                                    continue
                                (dataC5,out5)=dataOperation(dataC4, [e, out4])
                                if out5==-1:
                                    continue
                                output.append(out5)
                            phase.pop()
                        phase.pop()
                    phase.pop()
            print(max(output))


print("Answer for part one: ")
partOne()
