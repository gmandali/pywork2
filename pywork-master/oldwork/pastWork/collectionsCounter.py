# https://www.hackerrank.com/challenges/collections-counter/
from collections import Counter

n = int(input())
s = Counter(map(int, input().split()))
total = []
for item in range(int(input())):
    shoeSize, shoePrice = map(int, input().split())
    if s[shoeSize]:
        total.append(shoePrice)
        s.subtract(Counter([shoeSize]))


print(sum(total))
