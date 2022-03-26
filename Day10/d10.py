from math import gcd
from math import atan2

class Point:
    def __init__(self, x, y, norm, distance):
        self.x = x
        self.y = y
        self.norm = norm
        self.distance = distance
        self.angle = atan2(norm[0], norm[1])

inp = []
with open("input.txt", "r") as inputFile:
    inp = [[x for x in y.strip()] for y in inputFile.readlines()]
asteroids = set()
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == '#':
            asteroids.add((j, i))


ans1 = 0
chosenPoint = (0, 0)
sees = {}
for x1, y1 in asteroids:
    seen = {}
    for x2, y2 in asteroids:
        if (x1, y1) == (x2, y2):
            continue
        dx, dy = x2 - x1, y2 - y1
        norm = dx/gcd(dx, dy), dy/gcd(dx, dy)
        dist = dx**2 + dy**2
        p = Point(x2, y2, norm, dist)
        if norm in seen:
            if seen[norm].distance > p.distance:
                seen[norm] = p
        else:
            seen[norm] = p

    point = (x1, y1)
    sees[point] = seen.values()
    if len(sees[point]) > ans1:
        ans1 = len(sees[point])
        chosenPoint = point


ans2Point = sorted(sees[chosenPoint], key = lambda k: (k.angle, -1*k.distance), reverse = True)[199]


print(f"answer for partOne: {ans1}")
print(f"answer for partTwo: {ans2Point.x * 100 + ans2Point.y}")






