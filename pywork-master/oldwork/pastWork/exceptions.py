# https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
for num in range(int(input())):
    try:
        num1, num2 = map(int, input().split())
        print(num1//num2)
    except Exception as errorCode:
        print("Error Code:", errorCode)