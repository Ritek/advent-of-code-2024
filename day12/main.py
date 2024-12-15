from itertools import groupby
from collections import deque
from collections import defaultdict
from copy import deepcopy

fileContent = open("./input.txt", "r").readlines()
matrix = list(map(lambda line: list(line.replace("\n", "")), fileContent))

ROWS = len(matrix)
COLS = len(matrix[0])


def printMatrix():
    for row in matrix:
        print(row)


def checkNeighbours(pos, match):
    neighbours = set()
    diffNeigh = []
    y, x = pos

    if x+1 < COLS and matrix[y][x+1] == match:
        neighbours.add((y, x+1))
    else:
        diffNeigh.append((y, x+1))

    if x-1 >= 0 and matrix[y][x-1] == match:
        neighbours.add((y, x-1))
    else:
        diffNeigh.append((y, x-1))

    if y+1 < ROWS and matrix[y+1][x] == match:
        neighbours.add((y+1, x))
    else:
        diffNeigh.append((y+1, x))

    if y-1 >= 0 and matrix[y-1][x] == match:
        neighbours.add((y-1, x))
    else:
        diffNeigh.append((y-1, x))

    return (neighbours, diffNeigh)


def calcRegion(startPos):
    plots = []
    visited = set()
    plotType = matrix[startPos[0]][startPos[1]]
    diffNeighbours = []

    queue = deque()
    queue.append(startPos)

    while queue:
        curr = queue.popleft()

        if curr in visited:
            pass

        visited.add(curr)
        plots.append(curr)

        neigh, diffNeigh = checkNeighbours(curr, plotType)
        diffNeighbours.extend(diffNeigh)
        neigh -= visited
        for n in neigh:
            if n not in queue:
                queue.append(n)

    return (plots, visited, diffNeighbours)


printMatrix()


# better approach for finding length of the fence
def checkWalls(region):
    walls = 0
    for pos in region:
        y, x = pos

        if (y+1, x) not in region:
            walls += 1
        if (y, x+1) not in region:
            walls += 1
        if (y-1, x) not in region:
            walls += 1
        if (y, x-1) not in region:
            walls += 1

    return walls


def walkEdge(region):
    p = 0
    s = 0

    for i, (y, x) in enumerate(region):
        # Outer corners
        s += (y, x-1) not in region and (y-1, x) not in region
        s += (y, x+1) not in region and (y-1, x) not in region
        s += (y, x-1) not in region and (y+1, x) not in region
        s += (y, x+1) not in region and (y+1, x) not in region
        # Inner corners
        s += (y, x-1) in region and (y-1,
                                     x) in region and (y-1, x-1) not in region
        s += (y, x+1) in region and (y-1,
                                     x) in region and (y-1, x+1) not in region
        s += (y, x-1) in region and (y+1,
                                     x) in region and (y+1, x-1) not in region
        s += (y, x+1) in region and (y+1,
                                     x) in region and (y+1, x+1) not in region

    return s


visitedCells = set()
fenceTotal = 0
fenceCost = 0
for y, row in enumerate(matrix):
    for x, cell in enumerate(row):
        if (y, x) not in visitedCells:
            region, visited, fence = calcRegion((y, x))
            for v in visited:
                visitedCells.add(v)
            fenceTotal += len(region) * len(fence)
            print(matrix[y][x], walkEdge(region))
            fenceCost += len(region) * walkEdge(region)


print("Answer to question nr 1:", fenceTotal)
print("Answer to question nr 2:", fenceCost)
