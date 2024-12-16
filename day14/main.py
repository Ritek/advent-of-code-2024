inputContent = open("./input.txt", "r").read()
lines = inputContent.split("\n")[:-1]

ROWS = 103
COLS = 101
# ROWS = 7
# COLS = 11
#
ROWS_HALF = ROWS // 2
COLS_HALF = COLS // 2


def predictPos(pos, vel, time):
    x = (pos[0] + vel[0] * time) % COLS
    y = (pos[1] + vel[1] * time) % ROWS

    return (x, y)


q1 = 0
q2 = 0
q3 = 0
q4 = 0

for line in lines:
    splited = line.split(" ")
    px, py = map(int, splited[0][2:].split(","))
    vx, vy = map(int, splited[1][2:].split(","))

    origPos = (px, py)
    vel = (vx, vy)
    pos = predictPos(origPos, vel, 100)

    if pos[0] < COLS_HALF and pos[1] < ROWS_HALF:
        q1 += 1
    if pos[0] > COLS_HALF and pos[1] < ROWS_HALF:
        q2 += 1
    if pos[0] < COLS_HALF and pos[1] > ROWS_HALF:
        q3 += 1
    if pos[0] > COLS_HALF and pos[1] > ROWS_HALF:
        q4 += 1

print("Answer to question 1:", q1*q2*q3*q4)

# --- Answer to queston 2 ---


def renderMatrix(guards, index):
    matrix = [[" " for i in range(COLS)] for j in range(ROWS)]

    for guard in guards:
        x, y, *rest = guard
        matrix[y][x] = "*"

    shouldPrint = False
    for i, row in enumerate(matrix):
        # print(row, end="")
        x = "".join(row)
        if x.find("*******") > -1:
            shouldPrint = True
            break

    if shouldPrint:
        print("Answer to quesion 2:")
        print(index)
        for i, row in enumerate(matrix):
            print(row, end="")
            print()

        print("\n\n\n")


guards = []
for line in lines:
    splited = line.split(" ")
    px, py = map(int, splited[0][2:].split(","))
    vx, vy = map(int, splited[1][2:].split(","))
    guards.append([px, py, vx, vy])

for i in range(1, 20000):
    for guard in guards:
        pos = predictPos((guard[0], guard[1]), (guard[2], guard[3]), 1)
        guard[0] = pos[0]
        guard[1] = pos[1]

    renderMatrix(guards, i)
