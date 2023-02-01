# # https://www.hackerrank.com/challenges/text-wrap/problem
# # str = ABCDEFGHIJKLMNOPQRST
# # ABCDEF[0:6]
# # GHIJKL[6:12]
# # MNOPQR[12:18]
# # ST[18:24]
# # len = 20
# # max = 6, min = 0,
# # for letter in range(len)
# # take index (min and max+1)
# # (min+, max)
# import textwrap
#
# string = "ABCDEFGHIJKLMNOPQRST"
# width = 6
# idx1 = 0
# idx2 = width
# while idx1 <= len(string):
#     group = string[idx1:idx2]
#     idx1 += width
#     idx2 += width
#     print(group)
#
# idx1 = 0
# while idx1 <= len(string):
#     print(string[idx1:idx1+width])
#     idx1 += width
#
#
# for n in range(0, len(string), width):
#     print(string[n:n+width])


# import math
# f = math.ceil(n//width)
# for n in range(f+1):
#     print(string[n*width:(n * width)+width])

import textwrap
def wrap(strings, max_widths):
    return textwrap.fill(strings, max_widths)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)