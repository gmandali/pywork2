# https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true
num = int(input())
lis = set(input().split())
num1 = int(input())
lis1 = set(input().split())
print(len(lis.union(lis1)))