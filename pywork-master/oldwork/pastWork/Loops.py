# https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
n = int(input())
inca = n
for i in range(n):
    newNum = n - inca
    inca -= 1
    print(newNum**2)