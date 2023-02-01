# https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true
from itertools import combinations

inputList = input().split()
data = sorted(list((inputList[0])))
lens = int(inputList[1])
for x in range(lens):
    com = ["".join(myTuple)for myTuple in list(combinations(data, x+1))]
    print(*com, sep="\n")