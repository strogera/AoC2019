from collections import defaultdict
from math import ceil


class Ingredient:

    def __init__(self, name: str, amount: int) -> None:
        self.name = name
        self.amount = amount

class Recipie:

    def __init__(self, s: str = None) -> None:
        def getIngredient(s) -> Ingredient:
            c = s.strip().split(' ')
            return Ingredient(c[1].strip(), int(c[0]))

        ingr, res = s.strip().split('=>')
        self.ingredients = []
        self.result = getIngredient(res)
        for i in ingr.strip().split(','):
            self.ingredients.append(getIngredient(i))


with open("input.txt", "r") as inputFile:
    recipies = {}
    for line in inputFile.readlines():
        rec = Recipie(line)
        recipies[rec.result.name] = rec

    def getOreCost(numOfFuel=1):
        curRecipie = defaultdict(int)
        curRecipie['FUEL'] = numOfFuel
        while any(ingr != 'ORE' and curRecipie[ingr] > 0
                  for ingr in curRecipie.keys()):
            ingr = list(
                filter(lambda k: curRecipie[k] > 0 and k != 'ORE',
                       curRecipie.keys()))[0]
            made = recipies[ingr]
            modifiler = ceil(curRecipie[ingr] / made.result.amount)
            curRecipie[ingr] -= made.result.amount * modifiler
            for ingr in made.ingredients:
                curRecipie[ingr.name] += ingr.amount * modifiler
        return curRecipie['ORE']

    print(getOreCost(1))

    oreAvailable = 1000000000000
    upper = oreAvailable
    lower = 0
    result = 0
    while lower < upper:
        mid = (upper + lower) // 2
        ore = getOreCost(mid)
        if ore > oreAvailable:
            upper = mid - 1
        elif ore <= oreAvailable:
            result = lower
            lower = mid + 1
        else:
            break
    print(result)