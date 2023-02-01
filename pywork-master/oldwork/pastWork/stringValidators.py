# https://www.hackerrank.com/challenges/string-validators/problem

strInput = input()
print(any(c.isalnum() for c in strInput))
print(any(c.isalpha() for c in strInput))
print(any(c.isdigit() for c in strInput))
print(any(c.islower() for c in strInput))
print(any(c.isupper() for c in strInput))