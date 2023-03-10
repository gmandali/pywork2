# https://www.hackerrank.com/challenges/py-set-mutations/problem
# def performSetMutation(superSet, subSet, operation) -> set:
#     if operation == "update":
#         superSet.update(subSet)
#     elif operation == "intersection_update":
#         superSet.intersection_update(subSet)
#     elif operation == "difference_update":
#         superSet.difference_update(subSet)
#     elif operation == "symmetric_difference_update":
#         superSet.symmetric_difference_update(subSet)
#     return superSet


def getInputAndPerformOperation():
    global mainSet
    operationName, subSetLen = input().strip().split(" ")
    sideSet = set(map(int, input().strip().split(" ")[:int(subSetLen)]))
    # mainSet = performSetMutation(mainSet, sideSet, operationName.strip())
    try:
        # func = getattr(mainSet, operationName)
        # func(sideSet)
        operation = getattr(set, operationName)
        operation(mainSet, sideSet)
    except AttributeError:
        pass


mainSetLen = int(input().strip())
mainSet = set(map(int, input().strip().split(" ")[:mainSetLen]))
numberOfSubSets = int(input().strip())
[getInputAndPerformOperation() for repetitions in range(numberOfSubSets)]
setSum = sum(mainSet)
print(setSum)
