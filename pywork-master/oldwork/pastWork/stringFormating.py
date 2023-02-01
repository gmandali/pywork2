# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=false
def stringFormating(theNumber):
    width = len("{0:b}".format(theNumber))
    for i in range(1, theNumber + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))


stringFormating(input())
