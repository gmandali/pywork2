# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
NumOfElementsInSet = int(input())
MainSet = set(map(int, input().split()))
NumOfOperations = int(input())

for i in range(NumOfOperations):
    BigInput = input().split()
    if BigInput[0] == "pop":
        MainSet.pop()
    elif BigInput[0] == "discard":
        MainSet.discard(int(BigInput[1]))
    elif BigInput[0] == "remove":
        MainSet.remove(int(BigInput[1]))
print(sum(MainSet))
