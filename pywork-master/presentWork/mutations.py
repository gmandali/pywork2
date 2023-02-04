def mutate_string(string, position, character):
    string2 = list(string)
    string2[position] = character
    return "".join(string2)


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)
