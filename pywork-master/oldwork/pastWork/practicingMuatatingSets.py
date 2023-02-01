def performSetOperation(mainSet, allSet, operation) -> set:
    if operation == "update":
        mainSet.update(allSet)
    elif operation == "intersection_update":
        mainSet.intersection_update(allSet)
    elif operation == "difference_update":
        mainSet.difference_update(allSet)
    elif operation == "symmetric_update":
        mainSet.symmetric_update(allSet)
    else:
        print("Invalid operation")

    return mainSet


H = set("Gaurav")
R1 = set("Mandali")
R2 = set("Hi")
R3 = set("Gaurav")
performSetOperation(H, R1, "difference_update")
print(f"H.difference_update(R1) = {H}")
performSetOperation(H, R2, "intersection_update")
print(f"H.intersection_update(R2) = {H}")
performSetOperation(H, R3, "update")
print(f"H.union_update(R3) = {H}")
