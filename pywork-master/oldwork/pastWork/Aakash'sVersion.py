# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
from inspect import signature


def performSetOperation(dataSet, operation, element) -> set:
    try:
        # if operation == "pop":
        #     dataSet.pop()
        # elif operation == "remove":
        #     dataSet.remove(element)
        # elif operation == "discard":
        #     dataSet.discard(element)
        func = getattr(set, operation)
        func(dataSet, element)
        sig = signature(func)
        print(f'{operation} has {sig}')
    except BaseException as error:
        try:
            print(f'First Block: Operation Name: {operation}, error: {error}')
            func(dataSet)
        except AttributeError:
            print(f'Inner Block: Operation Name: {operation}, error: {error}')
        pass
    return dataSet


setSum = int(input())
infoSet = set(map(int, input().split()))
otherOperationLen = int(input())
for repetition in range(otherOperationLen):
    data = input().split()
    operationName = data[0]
    dataElement = int(data[1]) if len(data) > 1 else None
    infoSet = performSetOperation(infoSet, operationName.strip(), dataElement)
print(sum(infoSet))
