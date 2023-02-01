# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(s):
    stringAfterSwapped = s.swapcase()
    return stringAfterSwapped

s = input()
result = swap_case(s)
print(result)
