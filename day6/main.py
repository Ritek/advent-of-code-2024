import copy

inputFile = open("./input.txt", "r")
content = inputFile.read()

maze = list(map(list, content.split("\n")[:-1]))

ROWS = len(maze)
COLS = len(maze[0])

# --- solution for part 1 ---


def changeDirection():
    global direction
    if direction == "up":
        direction = "right"
    elif direction == "right":
        direction = "down"
    elif direction == "down":
        direction = "left"
    elif direction == "left":
        direction = "up"


def move():
    global guardX, guardY
    if direction == "up":
        guardY -= 1
    elif direction == "right":
        guardX += 1
    elif direction == "down":
        guardY += 1
    else:
        guardX -= 1


def isOut():
    return guardY < 0 or guardY >= ROWS or guardX < 0 or guardX >= COLS


def isOnObstacle():
    return maze[guardY][guardX] == "#" or maze[guardY][guardX] == "O"


def runSymulation():
    global guardY, guardX

    while True:
        prevY, prevX = guardY, guardX

        move()
        if isOut():
            return False

        if (guardY, guardX, direction) in path2:
            return True

        if isOnObstacle():
            guardY, guardX = prevY, prevX
            changeDirection()
        else:
            path.add((guardY, guardX))
            path2.add((guardY, guardX, direction))


# def runSymulationWithObstacle():
#     global guardY, guardX
#     visited = set()
#
#     while True:
#         prevY, prevX = guardY, guardX
#         # print(guardY, guardX)
#
#         move()
#         if isOut():
#             return False
#
#         if (guardY, guardX, direction) in visited:
#             return True
#
#         if isOnObstacle():
#             guardY, guardX = prevY, prevX
#             changeDirection()
#         else:
#             visited.add((guardY, guardX, direction))


# guardY, guardX = 6, 4
guardY, guardX = 36, 81
direction = "up"
path = set()
path2 = set()

runSymulation()

ans1 = len(set(path))
print("Answer to question 1:", ans1)

# --- Solution for part 2 ---

# ans2 = []
# for i, step in enumerate(path2):
#     print("testing {} out of {}".format(i, len(path2)))
#     # guardY, guardX = 6, 4
#     guardY, guardX = 36, 81
#     direction = "up"
#     obsY, obsX, dir = step
#
#     oldMaze = copy.deepcopy(maze)
#     if dir == "up" and obsY-1 > 0:
#         obsY -= 1
#     if dir == "right" and obsX < COLS-1:
#         obsX += 1
#     if dir == "down" and obsY < ROWS-1:
#         obsY += 1
#     if dir == "left" and obsX > 0:
#         obsX -= 1
#
#     maze[obsY][obsX] = "O"
#
#     looped = runSymulationWithObstacle()
#     if looped:
#         ans2.append((obsY, obsX))
#
#     maze = oldMaze
#
# print("Answer to question 2:", len(set(ans2)))
