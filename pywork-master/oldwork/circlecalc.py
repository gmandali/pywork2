print('This is for people who need a circle area and circumference calculator')
radius = float(input('What is the radius of the circle?: '))
this_or_that = str(input('would you like to find area or circumference?(c is fine for circumference): '))
if this_or_that in "area" or "circumference" or "c":
    if this_or_that in "area":
        print(radius ** 2 * 3.14)
    elif this_or_that in "circumference" or "c":
        print(radius * 3.14 * 2)
    else:
        print('sorry.')
else:
    print('You need to print one of those two words.')
