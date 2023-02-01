# from collections import OrderedDict
# dict = OrderedDict()
#
# company = input().split()
# for letter in range(len(company)):
#     if letter not in dict:
#         dict[letter] = letter
#     if letter in dict:
#         dict[letter] += letter
#     for key, value in dict.items():
#         print(key,value)

from collections import Counter

for letter in Counter(sorted(input())).most_common(3):
    print(*letter)