numOfStudents = int(input())
studDict = {}
for student in range(numOfStudents):
    line = input().split()
    name = line[0]
    marks = list(map(float, line[1:]))
    studDict[name] = marks


queryName = input()
values = studDict.get(queryName)
if values is None:
    print(f"{queryName} not found")
else:
    print("{:.2f}".format((sum(values)/len(values))))