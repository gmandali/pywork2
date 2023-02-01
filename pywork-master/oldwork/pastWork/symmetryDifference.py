# https://www.hackerrank.com/challenges/symmetric-difference/problem
l1 = int(input())
arr1 = set(map(int,input().split()))
l2 = int(input())
arr2 = set(map(int,input().split()))
first = arr1.difference(arr2)
second = arr2.difference(arr1)
answer = first.union(second)
sortedArray = sorted(answer)
print("\n".join(map(str,sortedArray)))
print("--------")
abc = [print(num) for num in sortedArray]
print(abc)