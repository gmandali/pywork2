# https://www.hackerrank.com/challenges/py-check-subset/problem

numberOfTestCases = int(input())
for number in range(numberOfTestCases):
    numberOfElements1 = int(input())
    set1 = set(input().split())
    numberOfElements2 = int(input())
    set2 = set(input().split())
    set1.issubset(set2)
    print(set1.issubset(set2))