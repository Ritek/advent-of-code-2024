fileContent = open("./input.txt", "r").read()

nums = list(fileContent.replace("\n", ""))
p1 = 0
p2 = len(nums) - 1
disc = []

while p1 <= p2:
    start = int(nums[p1])
    end = int(nums[p2])

    print(start, p1)
    print(end, p2)

    strToAdd = [p2 // 2]
    print("strToAdd", strToAdd)

    if p1 == 0 or p1 % 2 == 0:
        disc.extend(start * [p1 // 2])
        p1 += 1

    else:
        if start > end:
            print("start > end")
            disc.extend(end * strToAdd)
            nums[p1] = str(start - end)
            p2 -= 2
        elif start < end:
            print("start < end")
            disc.extend(start * strToAdd)
            nums[p2] = str(end - start)
            p1 += 1
        else:
            print("start == end")
            disc.extend(start * strToAdd)
            p1 += 1
            p2 -= 2


print(disc)

id = 0
for i, num in enumerate(disc):
    id += i * num

print(id)
