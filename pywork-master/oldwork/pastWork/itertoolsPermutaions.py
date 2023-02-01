#https://www.hackerrank.com/challenges/itertools-permutations/problem
from itertools import permutations
data, size = "HACK 2".split()
# data, size = input().split()
permutations = list(permutations(sorted(data), int(size)))
for item in permutations:
    print("".join(item))