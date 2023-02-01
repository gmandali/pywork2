# https://www.hackerrank.com/challenges/py-the-captains-room/problem?h_r=internal-search
from collections import Counter


num = int(input())
roomList = list(map(int, input().split()))
ct = Counter(roomList)
for key,number in ct.items():
    if number == 1:
        print(key)