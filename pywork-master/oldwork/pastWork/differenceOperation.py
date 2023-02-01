# https://www.hackerrank.com/challenges/py-set-difference-operation/problem?h_r=internal-search
num = int(input())
lis = set(input().split())
num1 = int(input())
lis1 = set(input().split())
print(len(lis.difference(lis1)))