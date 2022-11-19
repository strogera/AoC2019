from math import lcm


class Planet:

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.velx = 0
        self.vely = 0
        self.velz = 0

    def updateVelocity(self, p):

        def getVelocityIncrement(x: int, y: int) -> int:
            if (x > y):
                return -1
            if (x == y):
                return 0
            if (y > x):
                return 1

        self.velx += getVelocityIncrement(self.x, p.x)
        self.vely += getVelocityIncrement(self.y, p.y)
        self.velz += getVelocityIncrement(self.z, p.z)

    def updatePosition(self):
        self.x += self.velx
        self.y += self.vely
        self.z += self.velz

    def getEnergy(self):
        absSum = lambda a, b, c: abs(a) + abs(b) + abs(c)
        return absSum(self.x, self.y, self.z) * absSum(self.velx, self.vely,
                                                       self.velz)


with open("input.txt", "r") as inputFile:
    planets = [
        Planet(*[
            int(y.split('=')[1])
            for y in x.strip().replace('<', '').replace('>', '').split(',')
        ]) for x in inputFile.readlines()
    ]

    for _ in range(1000):
        for planet1 in planets:
            for planet2 in planets:
                planet1.updateVelocity(planet2)
        for planet1 in planets:
            planet1.updatePosition()
    print(sum([p.getEnergy() for p in planets]))

with open("input.txt", "r") as inputFile:
    planets = [
        Planet(*[
            int(y.split('=')[1])
            for y in x.strip().replace('<', '').replace('>', '').split(',')
        ]) for x in inputFile.readlines()
    ]
    seenXVelX = set()
    seenYVelY = set()
    seenZVelZ = set()
    i = 0
    xfound = False
    yfound = False
    zfound = False
    firstx = 0
    firsty = 0
    firstz = 0
    while not (xfound and yfound and zfound):
        for planet1 in planets:
            for planet2 in planets:
                planet1.updateVelocity(planet2)
        for planet1 in planets:
            planet1.updatePosition()
        if not xfound:
            statex = ''.join([str(x.x) + str(x.velx) for x in planets])
            if (statex in seenXVelX):
                firstx = i
                xfound = True
            seenXVelX.add(statex)
        if not yfound:
            statey = ''.join([str(x.y) + str(x.vely) for x in planets])
            if (statey in seenYVelY):
                firsty = i
                yfound = True
            seenYVelY.add(statey)
        if not zfound:
            statez = ''.join([str(x.z) + str(x.velz) for x in planets])
            if (statez in seenZVelZ):
                firstz = i
                zfound = True
            seenZVelZ.add(statez)

        i += 1
    print(lcm(firstx, firsty, firstz))
