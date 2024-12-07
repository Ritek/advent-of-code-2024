tests = open("./input.txt", "r").read().split("\n")


def checkWithBacktrack(numbers: [int], withConcat=False):
    results = []

    def backtrack(remaining: [int], tempValue: int):
        if len(remaining) == 0:
            results.append(tempValue)

        else:
            first = remaining[0]
            backtrack(remaining[1:], tempValue + first)
            backtrack(remaining[1:], tempValue * first)
            if withConcat:
                backtrack(remaining[1:], int(f"{tempValue}{first}"))

    backtrack(numbers[1:], numbers[0])
    return results


ans1 = 0
ans2 = 0
for test in tests[:-1]:
    result, *numbers = test.split(" ")
    result = int(result[:-1])
    numbers = list(map(int, numbers))

    outcomes = checkWithBacktrack(numbers, False)
    if result in outcomes:
        ans1 += result

    outcomes2 = checkWithBacktrack(numbers, True)
    if result in outcomes2:
        ans2 += result

print("Answer to question 1:", ans1)
print("Answer to question 2:", ans2)
