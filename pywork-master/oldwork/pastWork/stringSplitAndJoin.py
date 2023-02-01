# https://www.hackerrank.com/challenges/python-string-split-and-join/problem
def split_and_join(line):
    i = line.replace(" ", "-")
    return  i


line = input()
result = split_and_join(line)
print(result)