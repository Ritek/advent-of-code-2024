fileContent = open("./input2.txt", "r").read()
warehousePart, movesPart = fileContent.split("\n\n")

warehouse = []
moves = []
for line in warehousePart.split("\n"):
    warehouse.append(list(line))

moves = list(movesPart[:-1])


def printWarehouse(lines):
    for line in lines:
        print(line)


def moveBoxesVerticaly(pos, startRange, endRange, char="O"):
    for i in range(startRange, endRange):
        warehouse[i][pos[1]] = char


def moveBoxesHorizontaly(pos, startRange, endRange, char="O"):
    for i in range(startRange, endRange):
        warehouse[pos[0]][i] = char


def moveUp(pos):
    y, x = pos

    if (y-1, x) == ".":
        return (y-1, x)

    for i in range(y-1, 0, -1):
        if warehouse[i][x] == "#":
            return None
        if warehouse[i][x] == ".":
            moveBoxesVerticaly(pos, i, y-1)
            warehouse[y-1][x] = "."
            return (y-1, x)

    return False


def moveDown(pos):
    y, x = pos

    if (y+1, x) == ".":
        return (y+1, x)

    for i in range(y+1, len(warehouse)-1):
        if warehouse[i][x] == "#":
            return None
        if warehouse[i][x] == ".":
            moveBoxesVerticaly(pos, y+1, i+1)
            warehouse[y+1][x] = "."
            return (y+1, x)

    return False


def moveRight(pos):
    y, x = pos

    if (y, x+1) == ".":
        return (y, x+1)

    for i in range(x+1, len(warehouse[0])-1):
        if warehouse[y][i] == "#":
            return None
        if warehouse[y][i] == ".":
            moveBoxesHorizontaly(pos, x+1, i+1)
            warehouse[y][x+1] = "."
            return (y, x+1)

    return False


def moveLeft(pos):
    y, x = pos

    if (y, x-1) == ".":
        return (y, x-1)

    for i in range(x-1, -1, -1):
        if warehouse[y][i] == "#":
            return None
        if warehouse[y][i] == ".":
            moveBoxesHorizontaly(pos, i, x-1)
            warehouse[y][x-1] = "."
            return (y, x-1)

    return None


def findStart():
    for i, row in enumerate(warehouse):
        for j, col in enumerate(warehouse[0]):
            if warehouse[i][j] == "@":
                warehouse[i][j] = "."
                return (i, j)


(y, x) = findStart()
for move in moves:
    if move == "^":
        moved = moveUp((y, x))
    if move == ">":
        moved = moveRight((y, x))
    if move == "v":
        moved = moveDown((y, x))
    if move == "<":
        moved = moveLeft((y, x))

    if moved:
        y = moved[0]
        x = moved[1]


def calculateScore():
    score = 0

    for i, row in enumerate(warehouse):
        for j, col in enumerate(row):
            if warehouse[i][j] == "O":
                score += 100 * i + j

    return score


ans1 = calculateScore()
print("Answer to question 1:", ans1)

# --- Answer to part 2 ---

# warehouse = []
# for line in warehousePart.split("\n"):
#     line = list(line.replace("#", "##").replace("O", "[]").replace(
#         ".", "..").replace("@", "@."))
#     warehouse.append(line)
#
#
# def moveBigBoxesVerticaly(pos, startRange, endRange, char="O"):
#     y, x = pos
#     nextIdx = 1
#     if startRange < endRange:
#         nextIdx = -1
#
#     sx1 = x
#     sx2 = x+1
#     if warehouse[i][pos[1]] == "]":
#         sx2 = x-1
#
#     lines = dict()
#     for i in range(startRange, endRange, nextIdx):
#         if warehouse[i][pos[1]] == "[" and warehouse[i+nextIdx][pos[1]] == "[":
#             dict[i+nextIdx] = (sx1, sx2)
#         if warehouse[i][pos[1]] == "]" and warehouse[i+nextIdx][pos[1]] == "]":
#             dict[i+nextIdx] = (sx1, sx2)
#         if warehouse[i][pos[1]] == "[" and warehouse[i+nextIdx][pos[1]] == "]":
#             dict[i+nextIdx] = (sx1-1, sx2)
#         if warehouse[i][pos[1]] == "]" and warehouse[i+nextIdx][pos[1]] == "[":
#             dict[i+nextIdx] = (sx1, sx2+1)
#
#
# def moveBigUp(pos):
#     y, x = pos
#
#     if warehouse[y-1][x] == "[":
#         for i in range(y-1, 0, -1):
#             if warehouse[i][x] == "#":
#                 return False
#             if warehouse[i][x] == "." and warehouse[i][x+1] == ".":
#                 moveBoxesVerticaly(pos, i, y-1, "[")
#                 moveBoxesVerticaly((y, x+1), i, y-1, "]")
#                 warehouse[y-1][x] = "."
#                 warehouse[y-1][x+1] = "."
#                 return True
#
#     if warehouse[y-1][x] == "]":
#         for i in range(y-1, 0, -1):
#             if warehouse[i][x] == "#":
#                 return False
#             if warehouse[i][x] == "." and warehouse[i][x-1] == ".":
#                 moveBoxesVerticaly(pos, i, y-1, "]")
#                 moveBoxesVerticaly((y, x-1), i, y-1, "[")
#                 warehouse[y-1][x] = "."
#                 warehouse[y-1][x-1] = "."
#                 return True
#
#     return False
#
#
# def moveBigDown(pos):
#     y, x = pos
#
#     if warehouse[y+1][x] == "[":
#         for i in range(y+1, len(warehouse)-1):
#             if warehouse[i][x] == "#":
#                 return False
#             if warehouse[i][x] == "." and warehouse[i][x+1] == ".":
#                 moveBoxesVerticaly(pos, y+1, i+1, "[")
#                 moveBoxesVerticaly((y, x+1), y+1, i+1, "]")
#                 warehouse[y+1][x] = "."
#                 warehouse[y+1][x+1] = "."
#                 return (y+1, x)
#
#     if warehouse[y+1][x] == "]":
#         for i in range(y+1, len(warehouse)-1):
#             if warehouse[i][x] == "#":
#                 return False
#             if warehouse[i][x] == "." and warehouse[i][x-1] == ".":
#                 moveBoxesVerticaly(pos, y+1, i+1, "]")
#                 moveBoxesVerticaly((y, x-1), y+1, i+1, "[")
#                 warehouse[y+1][x] = "."
#                 warehouse[y+1][x-1] = "."
#                 return (y+1, x)
#
#     return False
#
#
# def moveBigRight(pos):
#     y, x = pos
#
#     if (y, x+1) == ".":
#         return (y, x+1)
#
#     for i in range(x+1, len(warehouse[0])-1):
#         if warehouse[y][i] == "#":
#             return None
#         if warehouse[y][i] == ".":
#             warehouse[y].pop(i)
#             warehouse[y].insert(x, ".")
#             return (y, x+1)
#
#     return False
#
#
# def moveBigLeft(pos):
#     y, x = pos
#
#     for i in range(x-1, -1, -1):
#         if warehouse[y][i] == "#":
#             return False
#         if warehouse[y][i] == ".":
#             warehouse[y].pop(i)
#             warehouse[y].insert(x, ".")
#             return (y, x-1)
#
#     return None
#
#
# printWarehouse(warehouse)
# print(moveBigRight((3, 3)))
# print()
# printWarehouse(warehouse)
