fileContent = open("./input2.txt", "r").read()


def moveBlocks(numbers):
    pointer1 = 0
    pointer2 = len(numbers)-1

    while pointer1 < pointer2:
        if numbers[pointer1] == "." and numbers[pointer2] != ".":
            numbers[pointer1] = numbers[pointer2]
            numbers[pointer2] = "."
            pointer1 += 1
            pointer2 -= 1
        elif numbers[pointer1] == "." and numbers[pointer2] == ".":
            pointer2 -= 1
        else:
            if pointer1 != ".":
                pointer1 += 1
            if pointer2 == ".":
                pointer2 -= 1

    return "".join(numbers).replace(".", "")


nums = list(fileContent.replace("\n", ""))
p1 = 0
p2 = len(nums)-1
disc = ""

print(nums)
while p1 < p2:
    start = int(nums[p1])
    end = int(nums[p2])

    print(start, p1)
    print(end, p2)

    if p1 == 0 or p1 % 2 == 0:
        disc += start * str(p1 // 2)
        p1 += 1

    else:
        strToAdd = str(p2 // 2)
        if start > end:
            print("start > end")
            disc += end * strToAdd
            nums[p1] = str(start - end)
            p2 -= 2
        elif start < end:
            print("start < end")
            disc += start * strToAdd
            nums[p2] = str(end - start)
            p1 += 1
        else:
            print("start == end")
            disc += start * strToAdd
            p1 += 1
            p2 -= 2

    print(disc)
    print()


print(disc)
