def find_max(num1,num2,num3,num4):
    numbers = [num1,num2,num3,num4]
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum