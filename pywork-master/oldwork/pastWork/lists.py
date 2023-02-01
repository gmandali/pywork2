# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
numOftimes = int(input())
newList = []
for i in range(numOftimes):
    operations = input().strip().split(" ")
    if operations[0] == "insert":
        newList.insert(int(operations[1]), int(operations[2]))
    elif operations[0] == "sort":
        newList.sort()
    elif operations[0] == "append":
        newList.append(int(operations[1]))
    elif operations[0] == "print":
        print(newList)
    elif operations[0] == "remove":
        newList.remove(int(operations[1]))
    elif operations[0] == "pop":
        newList.pop()
    elif operations[0] == "reverse":
        newList.reverse()