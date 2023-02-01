# https://www.hackerrank.com/challenges/maximize-it/problem?h_r=internal-search
from itertools import repeat
from itertools import product


def myFunction(data, modula):
    return sum(x * x for x in data) % modula


a, b = list(map(int,input().split()))
maximum = []
for currentList in range(a):
    something = list(map(int, input().split()[1:]))
    maximum.append(something)


result = list(product(*maximum))
finalResult = list(map(myFunction, result, repeat(b)))
print(max(finalResult))
