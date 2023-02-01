start, end = map(int, input().split())
numList = []
for i in range(start, end + 1):
    if i % 2 == 0:
        numList.append(i)

print(*numList)
