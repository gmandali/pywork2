# https://www.hackerrank.com/challenges/symmetric-difference/problem
length = int(input())
array = map(int, input().split())
length2 = int(input())
array2 = map(int, input().split())
setArr = set(array)
setArr2 = set(array2)
fullArr = setArr.union(setArr2)
sameNums = setArr.intersection(setArr2)
result = fullArr.difference(sameNums)
print('\n'.join(map(str, sorted(result))))