import re
import functools

inputFile = open("./input.txt", "r")
content = inputFile.read()

# --- question 1 ---
occurences = re.findall("mul\([0-9]+\,[0-9]+\)", content)


def reduceRow(row: str) -> int:
    temp = row.replace("mul(", "").replace(")", "").split(",")
    return int(temp[0]) * int(temp[1])


sum = functools.reduce(lambda a, b: a + reduceRow(b), occurences, 0)

print("Answer to queston 1:", sum)

# --- question 2 ---
occurences2 = re.findall("mul\([0-9]+\,[0-9]+\)|do\(\)|don\'t\(\)", content)

counts = True
sum2 = 0
for occurence in occurences2:
    if occurence == "don't()":
        counts = False
        continue
    if occurence == "do()":
        counts = True
        continue

    if counts:
        replaced = occurence.replace("mul(", "").replace(")", "")
        splited = replaced.split(",")
        sum2 += int(splited[0]) * int(splited[1])

print("Answer to queston 2:", sum2)
