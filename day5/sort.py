from functools import cmp_to_key

inputFile = open("./input.txt", "r")
content = inputFile.read()

rules, pages = content.split("\n\n")
rules = rules.split("\n")

dict = {}
for rule in rules:
    dict[rule] = 1


def getOrder(a, b):
    if f"{a}|{b}" in rules:
        return -1
    elif f"{b}|{a}" in rules:
        return 1
    else:
        return -1


corrects = []
incorrects = []
incorrectSorted = []
for update in pages.split("\n")[:-1]:
    temp = update.split(",")
    ordered = sorted(temp, key=cmp_to_key(lambda a, b: getOrder(a, b)))
    if temp == ordered:
        corrects.append(temp)
    else:
        incorrects.append(temp)
        incorrectSorted.append(ordered)

print("correct", corrects)
print("incorrect", incorrects)

sum1 = 0
for correct in corrects:
    sum1 += int(correct[len(correct) // 2])

print("Answer to question 1:", sum1)

sum2 = 0
for inc in incorrectSorted:
    sum2 += int(inc[len(inc) // 2])

print("Answer to question 2:", sum2)
