from itertools import accumulate

with open("input.txt", "r") as inputFile:
    input = inputFile.readline()
    basePattern = [0, 1, 0, -1]

    def getPattern(j, minLength):
        pat = []
        while len(pat) < minLength + 1:
            for c in basePattern:
                for _ in range(j):
                    pat.append(c)
        return pat[1:]

    curInput = [int(x) for x in input]
    for _ in range(100):
        newInput = []
        for j in range(len(curInput)):
            curPattern = getPattern(j + 1, len(curInput))
            s = 0
            for k, x in enumerate(curInput):
                s += x * curPattern[k]
            newInput.append(int(str(s)[-1]))
        curInput = newInput
    print(*curInput[:8], sep='')

    # Part 2 solution from
    # https://www.reddit.com/r/adventofcode/comments/ebai4g/comment/fb4tc12/?utm_source=share&utm_medium=web2x&context=3
    offset = int(input[:7])
    x = [int(x) for x in (input * 10000)[offset:][::-1]]

    for _ in range(100):
        x = list(accumulate(x, lambda a, b: (a + b) % 10))

    print(*x[::-1][:8], sep='')
