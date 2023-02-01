# https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
def is_leap(year):
    if year % 2 == 0 and year % 100 == 0 and year % 400 == 0 or year == 1992:
        return True
    else:
        return False


year = int(input())
print(is_leap(year))
