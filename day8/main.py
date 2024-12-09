from itertools import combinations
from itertools import chain
from copy import deepcopy

content = open("./input.txt", "r").read()

rows = content.split("\n")[:-1]
ROWS = len(rows)
COLS = len(rows[0])
print("ROWS:", ROWS)
print("COLS:", COLS)

singleLine = content.replace("\n", "")

matrix = list(map(lambda row: list(row), rows))


def printMatrix():
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            print(matrix[i][j], end="")
        print()


printMatrix()


def getPosition(index):
    return (index // ROWS, index % COLS)


def isValid(antinode):
    return -1 < antinode[0] < ROWS and -1 < antinode[1] < COLS


def getAntinodes(index1, index2):
    antinodes = []

    antinode1 = (index1[0] + (index1[0] - index2[0]),
                 index1[1] + (index1[1] - index2[1]))
    if isValid(antinode1):
        antinodes.append(antinode1)

    antinode2 = (index2[0] + (index2[0] - index1[0]),
                 index2[1] + (index2[1] - index1[1]))

    if isValid(antinode2):
        antinodes.append(antinode2)

    return antinodes


antenasDict = {}
for i, char in enumerate(singleLine):
    if char not in antenasDict and char != ".":
        antenasDict[char] = [getPosition(i)]
    elif char != ".":
        antenasDict[char].append(getPosition(i))

antenas = set(antenasDict.keys())

antinodes = set()
for key, values in antenasDict.items():
    temp = list(map(lambda x: getAntinodes(
        x[0], x[1]), list(combinations(values, 2))))
    temp = list(chain(*temp))
    antinodes.update(temp)

antinodes -= antenas

print("Answer to question 1:", len(antinodes))

# --- Solution for question 2 ---


def findAntinodes(index1, index2):
    antinodes = [index1, index2]

    diff1 = (index1[0] - index2[0], index1[1] - index2[1])
    diff2 = (diff1[0] * -1, diff1[1] * -1)

    def getNext(idx1, idx2):
        return (
            (idx1[0] + diff1[0], idx1[1] + diff1[1]),
            (idx2[0] + diff2[0], idx2[1] + diff2[1])
        )

    while True:
        ant1, ant2 = getNext(index1, index2)
        print("index1", index1, "index2", index2, ant1, ant2)
        isAnt1Valid = isValid(ant1)
        isAnt2Valid = isValid(ant2)
        if isAnt1Valid:
            antinodes.append(ant1)
            index1 = ant1
        if isAnt2Valid:
            antinodes.append(ant2)
            index2 = ant2

        if not isAnt1Valid and not isAnt2Valid:
            break

    print(antinodes)
    print()
    return antinodes


antinodes = []
for key, values in antenasDict.items():
    for combination in list(combinations(values, 2)):
        temp = findAntinodes(combination[0], combination[1])
        antinodes.append(temp)


temp = set(chain(*antinodes))

# for a in temp:
#     print("a", a)
#     matrix[a[0]][a[1]] = "#"
# printMatrix()
#
print("Answer to question 2:", len(temp))
