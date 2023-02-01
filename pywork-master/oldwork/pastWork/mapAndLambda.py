# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?h_r=internal-search
def fibonacci(n):
    fibList = [0, 1]
    for i in range(2, n):
        fibList.append(fibList[-1] + fibList[-2])

    return fibList[:n]


n = int(input())
print(list(map(lambda x: x ** 3, fibonacci(n))))
