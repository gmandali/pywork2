# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
from collections import OrderedDict
order = OrderedDict()
for i in range(int(input())):
    items = input().split()
    item1,item2 = " ".join(items[0:-1:]), items[-1]
    if item1 not in order:
        order[item1] = int(item2)
    else:
        order[item1] += int(item2)
for key, value in order.items():
    print(key,value)

