# https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
i = int(input())
if i % 2 != 0:
    print("Weird")
elif i in range(6,21) and i%2 == 0:
    print("Weird")
elif i in range(2,6) and i%2 == 0:
    print("Not Weird")
elif i>20 and i%2 == 0:
    print("Not Weird")