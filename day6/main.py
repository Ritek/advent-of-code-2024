inputFile = open("./input2.txt", "r")
content = inputFile.read()

maze = list(content.split("\n")[0:-1])

ROWS = len(maze)
COLS = len(maze[0])


# --- solution for part 1 ---
def printMaze():
    for y in range(0, ROWS):
        print("")
        for x in range(0, COLS):
            print(maze[y][x], end=" ")
    print()


def rotateMaze():
    global maze
    maze = list(zip(*maze[::-1]))


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
    return maze[guardY][guardX] == "#"


guardY, guardX = 6, 4
# guardY, guardX = 36, 81
direction = "up"
path = set()
path2 = set()

while True:
    prevY, prevX = guardY, guardX

    move()
    if isOut():
        break

    if isOnObstacle():
        guardY, guardX = prevY, prevX
        changeDirection()
    else:
        path.add(f"{guardY}|{guardX}")
        path2.add(f"{guardY}|{guardX}|{direction}")

ans1 = len(set(path))
print("Answer to question 1:", ans1)

# --- Solution for part 2 ---
