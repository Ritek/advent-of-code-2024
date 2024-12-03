from collections import Counter

inputFile = open("./input.txt", "r")
input = inputFile.read()
lines = input.split("\n")

list1 = []
list2 = []

for line in lines:
    temp = line.split("   ")
    if temp[0] and temp[1]:
        list1.append(int(temp[0]))
        list2.append(int(temp[1]))

list1.sort()
list2.sort()

# --- part 1 ---
ans = 0

for i, v in enumerate(list1):
    ans += abs(list2[i] - list1[i])

print("Answer to part 1:", ans)

# --- part 2 ---
locationDict = Counter(list2)

ans2 = 0
for num in list1:
    ans2 += (num * locationDict.get(num, 0))

print("Anser to part 2:", ans2)
