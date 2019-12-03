def manhattanDistance(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)


def partOne():
    with open("input.txt", "r") as inputFile:
        points=set()
        cross=set()
        for line in inputFile:
            x, y= 0, 0
            path=line.strip().split(',')
            curLinePoints=set()
            for direction in path:
                newx, newy=x, y
                if direction[0]=='R':
                    newx=x+int(direction[1:])
                    for xCord in range(x, newx):
                        curLinePoints.add((xCord,y))
                elif direction[0]=='L':
                    newx=x-int(direction[1:])
                    for xCord in range(x, newx, -1):
                        curLinePoints.add((xCord,y))
                elif direction[0]=='U':
                    newy=y+int(direction[1:])
                    for yCord in range(y, newy):
                        curLinePoints.add((x, yCord))
                elif direction[0]=='D':
                    newy=y-int(direction[1:])
                    for yCord in range(y, newy, -1):
                        curLinePoints.add((x, yCord))
                x=newx
                y=newy

            for (x, y) in curLinePoints:
                if (x, y) in points:
                    cross.add(manhattanDistance(x, y, 0, 0))
                else:
                    points.add((x, y))

        cross.remove(0) #remove starting point 

        print(min(cross))


def partTwo():
    with open("input.txt", "r") as inputFile:
        points=set()
        crossPoints=set()
        allpoints=[] 
        for line in inputFile:
            x, y= 0, 0
            path=line.strip().split(',')
            curLinePoints=set()
            curLinePointsL=[] #List of all points of the line path ordered
            for direction in path:
                newx, newy=x, y
                if direction[0]=='R':
                    newx=x+int(direction[1:])
                    for xCord in range(x, newx):
                        curLinePoints.add((xCord,y))
                        curLinePointsL.append((xCord,y))
                elif direction[0]=='L':
                    newx=x-int(direction[1:])
                    for xCord in range(x, newx, -1):
                        curLinePoints.add((xCord,y))
                        curLinePointsL.append((xCord,y))
                elif direction[0]=='U':
                    newy=y+int(direction[1:])
                    for yCord in range(y, newy):
                        curLinePoints.add((x, yCord))
                        curLinePointsL.append((x,yCord))
                elif direction[0]=='D':
                    newy=y-int(direction[1:])
                    for yCord in range(y, newy, -1):
                        curLinePoints.add((x, yCord))
                        curLinePointsL.append((x,yCord))
                x=newx
                y=newy

            for (x, y) in curLinePoints:
                if (x, y) in points:
                    crossPoints.add((x, y))
                else:
                    points.add((x, y))
            allpoints.append(curLinePointsL)

        pathLengthToCrossPoint=[]
        for (x, y) in crossPoints:
            if(x, y)==(0,0):
                continue
            curPathLength=0
            for i in range (len(allpoints)):
                curPathLength+=len(allpoints[i][0:allpoints[i].index((x, y))])
            pathLengthToCrossPoint.append(curPathLength)

        print(min(pathLengthToCrossPoint))



print("Answer for part one: ")
partOne()
print("Answer for part two: ")
partTwo()
