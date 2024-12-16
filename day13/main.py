import re

# copied from https://www.youtube.com/watch?v=-5J-DAsWuJc
fileContent = open("input.txt", "r").read()
machinesInfo = fileContent.split("\n\n")


total = 0
for machineInfo in machinesInfo:
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", machineInfo))
    print(ax, ay, bx, by, px, py)

    px += 10000000000000
    py += 10000000000000

    countOfApress = (px * by - py * bx) / (ax * by - ay * bx)
    countOfBpress = (px - ax * countOfApress) / bx
    print(countOfApress, countOfBpress)

    if (countOfApress % 1 == 0) and (countOfBpress % 1 == 0):
        total += countOfApress * 3 + countOfBpress

print(total)
