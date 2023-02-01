# https://www.hackerrank.com/challenges/py-check-strict-superset/problem
def functionY(mainSet, otherSets) -> bool:
    if mainSet.issuperset(otherSets) and not otherSets.issuperset(mainSet):
        print(otherSets.issuperset(mainSet))
    else:
        return False


result = True
mainSet = set(input().strip().split())
numberOfOtherSets = int(input())
for i in range(numberOfOtherSets):
    otherSet = set(input().strip().split())
    if result:
        if not functionY(mainSet, otherSet):
            result = False

print(result)
