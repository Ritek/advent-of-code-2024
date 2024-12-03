from collections.abc import Callable

inputFile = open("./input.txt", "r")
input = inputFile.read()
lines = input.split("\n")

reports = []

for line in filter(lambda line: line != "", lines):
    numbers = [int(n) for n in line.split(" ")]
    reports.append(numbers)


# --- Question 1 ---
CallbackType: Callable[[int], bool] = None


def isSafe(numbers: [int]) -> bool:
    def isSequence(numbers: [int], condition: CallbackType) -> bool:
        return all(
            condition(a, b) and 0 < abs(a-b) <= 3
            for a, b in zip(numbers, numbers[1:])
        )

    return isSequence(numbers, lambda a, b: a > b) or isSequence(
        numbers, lambda a, b: a < b)


ans1 = 0
for report in list(filter(isSafe, reports)):
    ans1 += 1

print("Anser to question 1:", ans1)

# --- Question 2 ---


def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False


ans2 = sum([
    any([
        is_safe(row[:i] + row[i + 1:]) for i in range(len(row))
    ]) for row in reports
])

print("Anser to question 2:", ans2)


def twoPointers(numbers):
    i = 1
    lastSafe = 0
    safe = True

    while i < len(numbers)-1:
        if abs(numbers[i] - numbers[lastSafe]) == 0 or abs(numbers[i] - numbers[lastSafe]) > 3:
            if safe:
                safe = False
            else:
                return False
        elif numbers[lastSafe] < numbers[i] > numbers[i+1] or numbers[lastSafe] > numbers[i] < numbers[i+1]:
            if safe:
                safe = False
            else:
                return False
        else:
            lastSafe = i
        i += 1
    return True


ans3 = 0
for report in list(filter(twoPointers, reports)):
    ans3 += 1

print("Answer to question 2 (v2):", ans3)
