fileContent = open("./input2.txt", "r").read()

nums = list(fileContent.replace("\n", ""))

# --- Solution for part 1 ---
p1 = 0
p2 = len(nums) - 1
disc = []

while p1 <= p2:
    start = int(nums[p1])
    end = int(nums[p2])

    strToAdd = [p2 // 2]

    if p1 == 0 or p1 % 2 == 0:
        disc.extend(start * [p1 // 2])
        p1 += 1

    else:
        if start > end:
            disc.extend(end * strToAdd)
            nums[p1] = str(start - end)
            p2 -= 2
        elif start < end:
            disc.extend(start * strToAdd)
            nums[p2] = str(end - start)
            p1 += 1
        else:
            disc.extend(start * strToAdd)
            p1 += 1
            p2 -= 2

id = 0
for i, num in enumerate(disc):
    id += i * num

print("Answer to question 1:", id)

# --- Solution for part 2 ---
nums = list(fileContent.replace("\n", ""))
queue = []


for i, num in enumerate(nums):
    currentInt = int(nums[i])

    if i == 0 or i % 2 == 0:
        chunk = "".join(currentInt * str(i // 2))
        queue.append(chunk)
    else:
        chunk = "".join(currentInt * ".")
        if chunk != "":
            queue.append(chunk)


def findSpace(before, length):
    for i in range(0, before):
        if "." in queue[i] and len(queue[i]) >= length:
            return (i, len(queue[i]) - length)


p1 = 0
p2 = len(queue) - 1
while p2 > 0:
    space = findSpace(p2, len(queue[p2]))
    if space:
        index = space[0]
        length = space[1]
        newNodes = [queue[p2], "." * length]
        queue[p2] = len(queue[p2]) * "."

        queue.pop(index)
        if newNodes[1] != "":
            queue.insert(index, newNodes[1])
        queue.insert(index, newNodes[0])

    p2 -= 1


temp = "".join(queue)
id = 0
for i, val in enumerate(list(temp)):
    if "." not in val:
        id += i * int(val)

print("Answer to question 2:", id)
