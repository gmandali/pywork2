def selectionSorter(array):
    for idx in range(len(array)):
        minimum = idx
        for idx2 in range(idx, len(array)):
            if array[minimum] > array[idx2]:
                minimum = idx2
        array[idx], array[minimum] = array[minimum], array[idx]
    return array


numsList = [5, 55, 52, 32, 33, -2, 67, 88]
maxNum = numsList[0]
for num in numsList:
    if maxNum < num:
        maxNum = num
print(*selectionSorter(numsList))
