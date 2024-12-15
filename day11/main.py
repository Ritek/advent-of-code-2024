import itertools
from collections import defaultdict

content = open("input.txt", "r").read()
nums = content.replace("\n", "").split(" ")
nums = list(map(int, nums))


def transform(num: int):
    numStr = str(num)
    length = len(numStr)

    if num == 0:
        return [1]

    elif length % 2 == 0:
        temp1, temp2 = numStr[0:length//2], numStr[length//2:length]
        return [int(temp1), int(temp2)]

    else:
        return [num * 2024]


def recTransf(nums: [int], blinkLimit: int, blinkCount: int = 1):
    newNums = list(itertools.chain(*[transform(num) for num in nums]))

    if blinkCount < blinkLimit:
        return recTransf(newNums, blinkLimit, blinkCount + 1)
    else:
        return newNums


ans1 = recTransf(nums, 25)
print("Answer to question 1:", len(ans1))

# --- Solution for part 2 ---

stones = defaultdict(int)
for num in nums:
    stones[num] += 1


def blink_times(blinks):
    for i in range(blinks):
        blink()
        print(i, len(stones))
    return


def blink():
    stonework = dict(stones)
    for stone, count in stonework.items():
        if count == 0:
            continue
        if stone == 0:
            stones[1] += count
            stones[0] -= count
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            new_len = int(len(stone_str) / 2)
            stone_1 = int(stone_str[:new_len])
            stone_2 = int(stone_str[new_len:])
            stones[stone_1] += count
            stones[stone_2] += count
            stones[stone] -= count
        else:
            stones[stone * 2024] += count
            stones[stone] -= count
    return


blink_times(75)
print("Answer to question 2:", sum(stones.values()))
