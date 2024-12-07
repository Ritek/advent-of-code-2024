tests = open("./input.txt", "r").read().split("\n")


def checkWithBacktrack(numbers: [int]):
    results = []

    def backtrack(remaining: [int], tempValue: int, target=0):
        if tempValue == target:
            results.append(target)
            return

        if len(remaining) == 0:
            results.append(tempValue)
        else:
            first = remaining[0]
            backtrack(remaining[1:], tempValue + first)
            backtrack(remaining[1:], tempValue * first)
            backtrack(remaining[1:], int(f"{tempValue}{first}"))

    first = numbers.pop(0)
    backtrack(numbers, first)
    return results


ans1 = 0
for test in tests[:-1]:
    result, *numbers = test.split(" ")
    result = int(result[:-1])
    numbers = list(map(int, numbers))
    outcomes = checkWithBacktrack(numbers)
    if result in outcomes:
        ans1 += result

print("Answer to question 1:", ans1)
