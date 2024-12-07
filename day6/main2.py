import copy


class Symulation:
    direction = "up"

    def __init__(self, maze, guardY, guardX):
        self.guardY = guardY
        self.guardX = guardX
        self.maze = maze
        self.ROWS = len(self.maze)
        self.COLS = len(self.maze[0])
        self.visited = []
        self.distinctPositions = set()

    def printMaze(self):
        for y in range(0, self.ROWS):
            print("")
            for x in range(0, self.COLS):
                print(self.maze[y][x], end=" ")
        print()

    def changeDirection(self):
        if self.direction == "up":
            self.direction = "right"
        elif self.direction == "right":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "left"
        else:
            self.direction = "up"

    def move(self):
        if self.direction == "up":
            self.guardY -= 1
        elif self.direction == "right":
            self.guardX += 1
        elif self.direction == "down":
            self.guardY += 1
        else:
            self.guardX -= 1

    def isOut(self):
        return self.guardY < 0 or self.guardY >= self.ROWS or self.guardX < 0 or self.guardX >= self.COLS

    def isOnObstacle(self):
        return self.maze[self.guardY][self.guardX] == "#" or self.maze[self.guardY][self.guardX] == "O"

    def runSymulation(self):
        visited = set()
        while True:
            prevY, prevX = self.guardY, self.guardX

            self.move()
            if self.isOut():
                return False

            if (self.guardY, self.guardX, self.direction) in visited:
                return True

            if self.isOnObstacle():
                self.guardY, self.guardX = prevY, prevX
                self.changeDirection()
            else:
                self.distinctPositions.add(
                    (self.guardY, self.guardX))
                visited.add((self.guardY, self.guardX, self.direction))


# --- Solution for part 1 ---
testInput = open("./input2.txt", "r").read()
maze = list(map(list, testInput.split("\n")[:-1]))
questonTest = Symulation(maze, 6, 4)
questonTest.runSymulation()
print("Test:", len(questonTest.distinctPositions))

input = open("./input.txt", "r").read()
maze = list(map(list, input.split("\n")[:-1]))
queston1 = Symulation(maze, 36, 81)
queston1.runSymulation()
print("Answer to question 1:", len(queston1.distinctPositions))

# --- Solution for part 2 ---
ans2 = 0
# ans2Debug = []
input = open("./input.txt", "r").read()
maze = list(map(list, input.split("\n")[:-1]))
for i, step in enumerate(queston1.distinctPositions):
    print("{} / {}".format(i, len(queston1.distinctPositions)))
    mazeCopy = copy.deepcopy(maze)
    mazeCopy[step[0]][step[1]] = "O"
    queston2 = Symulation(mazeCopy, 36, 81)
    looped = queston2.runSymulation()
    if looped:
        # ans2Debug.append(queston2)
        ans2 += 1

print("Answer to question 2:", ans2)
# for a in ans2Debug:
#     print(a.printMaze())
