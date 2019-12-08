
def partOne():
    with open("input.txt", "r") as inputFile:
        width=25
        height=6
        for line in inputFile:
            pic=[]
            countLayers=0
            countRows=0
            layer=[]
            while line:
                row=line[:width]
                line=line[width:]
                layer.append(row)
                countRows+=1
                if countRows==height:
                    pic.append(layer)
                    countLayers+=1
                    countRows=0
                    layer=[]
            layerPtr=[]
            minZero=1000000
            for l in pic:
                zero=len([x for y in l for z in y for x in z if x=='0'])
                if zero<=minZero:
                    minZero=zero
                    layerPtr=list(l)
            print(len([x for y in layerPtr for z in y for x in z if x=='1'])*len([x for y in layerPtr for z in y for x in z if x=='2']))
                






def partTwo():
    with open("input.txt", "r") as inputFile:
        width=25
        height=6
        for line in inputFile:
            pic=[]
            countLayers=0
            countRows=0
            layer=[]
            while line:
                row=list(line[:width])
                line=line[width:]
                layer.append(row)
                countRows+=1
                if countRows==height:
                    pic.append(layer)
                    countLayers+=1
                    countRows=0
                    layer=[]
            for h in range(height):
                for w in range(width):
                    pixel=pic[0][h][w]
                    for x in range(countLayers):
                        if pixel!='2':
                            break
                        else:
                            pixel=pic[x][h][w]
                    pic[0][h][w]=pixel
            print('\n'.join([''.join(x) for x in pic[0]]).replace('0', ' '))

                            



print("Answer for part one: ")
partOne()
print("Answer for part two: ")
partTwo()
