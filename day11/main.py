import itertools

content = open("input.txt", "r").read()
nums = content.replace("\n", "").split(" ")

print(nums)


def transform(num: str):
    length = len(num)

    if num == "0":
        return ["1"]

    elif length % 2 == 0:
        chunks, chunk_size = length, length//2
        temp = [num[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
        return [str(int(temp[0])), str(int(temp[1]))]

    else:
        return [str(int(num) * 2024)]


def recTransf(nums: [str], blinkLimit: int, blinkCount: int = 1):
    print(blinkCount, " / ", blinkLimit)
    newNums = list(itertools.chain(*[transform(num) for num in nums]))

    if blinkCount < blinkLimit:
        return recTransf(newNums, blinkLimit, blinkCount + 1)
    else:
        return newNums


ans1 = recTransf(nums, 25)
print("Answer to question 1:", len(ans1))
# ans2 = recTransf(nums, 75)
# print("Answer to question 2:", len(ans2))
