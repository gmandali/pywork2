# https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    newStr = list(string)
    newStr[position] = character
    return "".join(newStr)


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)