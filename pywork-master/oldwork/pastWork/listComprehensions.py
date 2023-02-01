# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
x = int(input())
y = int(input())
z = int(input())
n = int(input())
numList = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                numList.append([i,j,k])

print(numList)
