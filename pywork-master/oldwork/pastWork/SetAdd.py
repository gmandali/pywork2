# https://www.hackerrank.com/challenges/py-set-add/problem
# this is the my version
# countries = set()
# for i in range(int(input())):
#     countries.add(input())
#
# print(len(countries))
print(len(set([input() for i in range(int(input()))])))