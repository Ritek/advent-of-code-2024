from copy import deepcopy

content = open("./input.txt", "r").read().split("\n")[:-1]
oneLine = list(open("./input.txt", "r").read().replace("\n", ""))

ROWS = len(content)
COLS = len(list(content[0]))

matrix = []
startPos = []
for y, height in enumerate(oneLine):
    if height == "0":
        startPos.append((y // ROWS, y % COLS))

for row in content:
    matrix.append([int(x) for x in list(row)])


def printMatrix():
    for row in matrix:
        print(list(row))


# printMatrix()


def checkNeightbours(startPos, value):
    check = set()
    x, y = startPos
    if x+1 < COLS and matrix[x+1][y] == value:
        check.add((x+1, y))
    if x-1 >= 0 and matrix[x-1][y] == value:
        check.add((x-1, y))
    if y+1 < ROWS and matrix[x][y+1] == value:
        check.add((x, y+1))
    if y-1 >= 0 and matrix[x][y-1] == value:
        check.add((x, y-1))

    return check


def findPaths(pos):
    paths = []
    paths2 = []

    def findPathsInner(pos, path, visited):
        y, x = pos
        val = matrix[y][x]

        if val == 9:
            if pos not in paths:
                paths.append(pos)
            paths2.append(path)
            return

        neigh = checkNeightbours(pos, val+1)
        neigh -= visited

        for n in neigh:
            findPathsInner(n, deepcopy(path) + [pos], visited.union([pos]))

    findPathsInner(pos, [], set())
    return [paths, paths2]


ans = 0
ans2 = 0
for start in startPos:
    temp = findPaths(start)
    ans += len(temp[0])
    ans2 += len(temp[1])

print("Answer to question 1:", ans)
print("Answer to question 2:", ans2)
