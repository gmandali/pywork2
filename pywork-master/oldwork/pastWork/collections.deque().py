# https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true
from collections import deque

i = deque()
for num in range(int(input())):
    a = input().split()
    if a[0] == "append":
        i.append(a[1])
    elif a[0] == "pop":
        i.pop()
    elif a[0] == "appendleft":
        i.appendleft(a[1])
    elif a[0] == "popleft":
        i.popleft()

print(*i)
