def bubbleSorter(array):
    arrayLength = len(array)
    for idx in range(arrayLength - 1):
        for idx2 in range(arrayLength - idx - 1):
            if array[idx2] > array[idx2 + 1]:
                array[idx2], array[idx2 + 1] = array[idx2 + 1], array[idx2]
    return array


numsList = [5, 55, 52, 32, 33, -2, 67, 88]
maxNum = numsList[0]
for num in numsList:
    if maxNum < num:
        maxNum = num
print(*bubbleSorter(numsList))
