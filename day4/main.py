inputFile = open("input.txt", "r")
content = inputFile.read()

contentArr = [list(row) for row in [row for row in content.split("\n")]]

ROW_NUM = len(contentArr)
ROW_LENGTH = len(contentArr[0])

# --- Answer to part 1 ---


def findWord(x: int, y: int) -> [int]:
    if contentArr[x][y] != "X" and contentArr[x][y] != "S":
        return []

    words = []

    wordRow = "".join(contentArr[x][y:y+4])
    if wordRow == "XMAS" or wordRow == "SAMX":
        words.append(wordRow)
        pass

    if x < ROW_NUM - 4:
        wordCol = "".join([contentArr[x+i][y] for i in range(0, 4)])
        if wordCol == "XMAS" or wordCol == "SAMX":
            words.append(wordCol)
        pass

    if x < ROW_NUM - 4 and y < ROW_LENGTH - 3:
        wordCross = "".join([contentArr[x+i][y+i] for i in range(0, 4)])
        if wordCross == "XMAS" or wordCross == "SAMX":
            words.append(wordCross)

    if x < ROW_NUM - 4 and y >= 3:
        wordCross = "".join([contentArr[x+i][y-i] for i in range(0, 4)])
        if wordCross == "XMAS" or wordCross == "SAMX":
            words.append(wordCross)

    return words


# def findWord2() -> [int]:
#     count = 0
#
#     for row in contentArr:
#         count += row.count("XMAS")
#         count += row.count("SAMX")
#
#     columns = list(zip(*contentArr))
#     for col in columns:
#         count += col.count("XMAS")
#         count += col.count("SAMX")
#
#     diagMain = [contentArr[len(contentArr-1-i)][i]
#                 for i in range(0, len(contentArr)-1)]
#     for diag in diagMain:
#         count += diag.count("XMAS")
#         count += diag.count("SAMX")
#
#     diagSec = [contentArr[i][len(contentArr)-i-1]
#                for i in range(len(contentArr))]
#     for diag in diagMain:
#         count += diag.count("XMAS")
#         count += diag.count("SAMX")
#
#     return count


ans = 0
for x, row in enumerate(contentArr):
    for y, char in enumerate(row):
        ans += len(findWord(x, y))

print("Answer to question 1:", ans)

# --- Answer to part 2 ---


def isCross(x: int, y: int) -> bool:
    if contentArr[x][y] == "A":
        one = contentArr[x-1][y-1] + contentArr[x][y] + contentArr[x+1][y+1]
        two = contentArr[x+1][y-1] + contentArr[x][y] + contentArr[x-1][y+1]

        if (one == "MAS" or one == "SAM") and (two == "MAS" or two == "SAM"):
            return True

    return False


ans2 = 0
for x in range(1, len(contentArr)-2):
    for y in range(1, len(contentArr[0])-1):
        if isCross(x, y):
            ans2 += 1

print("Answer to question 2:", ans2)
