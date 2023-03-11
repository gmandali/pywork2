equation = input("Enter the quadratic equation: ")
aVal = int(input("Enter the 'a' value: "))
bVal = int(input("Enter the 'b' value: "))
cVal = int(input("Enter the 'c' value: "))
solution1 = -abs(bVal) + ((bVal ** 2 - 4 * aVal * cVal)**1/2)
solution2 = -abs(bVal) - ((bVal ** 2 - 4 * aVal * cVal)**1/2)
if solution1 == solution2:
    print("The roots for the quadratic equation: y =", equation, "is:", solution1 / 2)
elif solution1 != solution2:
    print("The roots for the quadratic equation: y =", equation, "are:", solution1 / 2, "and", solution2 / 2)
else:
    print("No solution present in the given equation")
