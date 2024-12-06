from typing import Dict

inputFile = open("./input.txt", "r")
content = inputFile.read()

parts = content.split("\n\n")
ordering = parts[0]
updates = parts[1]

dict: Dict[int, [int]] = {}

for order in ordering.split("\n"):
    nums = tuple(map(int, order.split("|")))
    value = nums[0]
    after = nums[1]

    if value in dict:
        dict.get(value).append(after)
    else:
        dict[value] = [after]


def isCorrect(nums: [int]):
    for i in range(1, len(nums)):
        if nums[i] in dict:
            s1 = set(dict[nums[i]])
            s2 = set(nums[0:i])

            matches = s1.intersection(s2)
            if len(matches) > 0:
                return False
    return True


corrects = []
incorrects = []
for update in updates.split("\n")[:-1]:
    nums = tuple(map(int, update.split(",")))

    if isCorrect(nums):
        corrects.append(nums)
    else:
        incorrects.append(nums)

ans = 0
for correct in corrects:
    ans += correct[len(correct) // 2]

print("Answer to question 1:", ans)


# --- Solution to question 2 ---
incorrects = list(map(list, incorrects))
for incorrect in incorrects:
    for i in range(1, len(incorrect)):
        if incorrect[i] in dict:
            s1 = set(dict[incorrect[i]])
            matches = [x for x in incorrect[0:i] if x in s1]

            for match in matches:
                index = incorrect.index(match)
                temp = incorrect[i]
                incorrect[i] = match
                incorrect[index] = temp

ans = 0
for incorrect in incorrects:
    ans += incorrect[len(incorrect) // 2]

print("Answer to question 2:", ans)
