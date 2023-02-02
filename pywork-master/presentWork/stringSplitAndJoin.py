def split_and_join(line2):
    return "-".join(line2.split(" "))


line = input()
result = split_and_join(line)
print(result)
