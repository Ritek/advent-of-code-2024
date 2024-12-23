import heapq
from collections import deque
from copy import deepcopy

fileContent = open("./input.txt", "r").read()

lines = fileContent.split("\n")[:-1]
ROWS = len(lines)
COLS = len(lines[0])

maze = []

for i, row in enumerate(lines):
    arr = list(row)
    maze.append(arr)

startPos = (ROWS-2, 1)
endPos = (1, COLS-2)


def printMaze():
    for i, row in enumerate(maze):
        print(row)


def checkPath(pos):
    y, x = pos
    paths = set()

    if maze[y+1][x] != "#":
        paths.add((y+1, x))
    if maze[y][x+1] != "#":
        paths.add((y, x+1))
    if maze[y][x-1] != "#":
        paths.add((y, x-1))
    if maze[y-1][x] != "#":
        paths.add((y-1, x))

    return paths


# def dijkstra(grid, starts):
#     delta = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}
#
#     dist = {}
#     pq = []
#     for sr, sc, dir in starts:
#         dist[(sr, sc, dir)] = 0
#         heapq.heappush(pq, (0, sr, sc, dir))
#
#     while pq:
#         (d, row, col, direction) = heapq.heappop(pq)
#         if dist[(row, col, direction)] < d:
#             continue
#
#         for next_dir in "EWNS".replace(direction, ""):
#             if (row, col, next_dir) not in dist or dist[(row, col, next_dir)] > d + 1000:
#                 dist[(row, col, next_dir)] = d + 1000
#                 heapq.heappush(pq, (d + 1000, row, col, next_dir))
#
#         dr, dc = delta[direction]
#         next_row, next_col = row + dr, col + dc
#         if (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0])
#             and grid[next_row][next_col] != "#"
#             and (
#                 (next_row, next_col, direction) not in dist
#                 or dist[(next_row, next_col, direction)] > d + 1
#         )):
#             dist[(next_row, next_col, direction)] = d + 1
#             heapq.heappush(pq, (d + 1, next_row, next_col, direction))
#
#     return dist


def dijkistra(grid, starts):
    delta = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}

    adjecency = {}
    pq = []

    for sr, sc, dir in starts:
        adjecency[(sr, sc, dir)] = 0
        heapq.heappush(pq, (0, sr, sc, dir))

    while pq:
        (time, row, col, direction) = heapq.heappop(pq)
        if adjecency[(row, col, direction)] < time:
            continue

        for nextDir in "EWNS".replace(direction, ""):
            if (row, col, nextDir) not in adjecency or adjecency[(row, col, nextDir)] > time + 1000:
                adjecency[(row, col, nextDir)] = time + 1000
                heapq.heappush(pq, (time + 1000, row, col, nextDir))

        dr, dc = delta[direction]
        nextRow, nextCol = row + dr, col + dc
        if (0 <= nextRow < ROWS and 0 <= nextCol < COLS
                and grid[nextRow][nextCol] != "#"
                and (
                    (nextRow, nextCol, direction) not in adjecency
                    or adjecency[(nextRow, nextCol, direction)] > time + 1
                )):
            adjecency[(nextRow, nextCol, direction)] = time + 1
            heapq.heappush(pq, (time + 1, nextRow, nextCol, direction))

    return adjecency


def parse(lines):
    grid = []
    line = 0
    for line in range(len(lines)):
        grid.append(list(lines[line].strip()))

    s = None
    e = None
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "S":
                s = (r, c)
            elif ch == "E":
                e = (r, c)
    return grid, s, e


def part1(input):
    grid, (sr, sc), (er, ec) = input
    dist = dijkistra(grid, [(sr, sc, "E")])
    best = 1000000000
    for dir in "EWNS":
        if (er, ec, dir) in dist:
            best = min(best, dist[(er, ec, dir)])
    return best


def part2(input):
    grid, (sr, sc), (er, ec) = input

    bestFromStart = dijkistra(grid, [(sr, sc, "E")])
    bestFromEnd = dijkistra(grid, [(er, ec, d) for d in "EWNS"])
    optimal = part1(input)
    result = set()
    flip = {"E": "W", "W": "E", "N": "S", "S": "N"}

    for row in range(ROWS):
        for col in range(COLS):
            for dir in "EWNS":
                stateFromStart = (row, col, dir)
                stateFromEnd = (row, col, flip[dir])

                if stateFromStart in bestFromStart and stateFromEnd in bestFromEnd:
                    if bestFromStart[stateFromStart] + bestFromEnd[stateFromEnd] == optimal:
                        result.add((row, col))
    return len(result)


input = parse(open("./input.txt", "r").readlines())
print(part1(input))
print(part2(input))
