import random

entry = input("Enter your statement you want the magic 8 ball to comprehend: ")
num = random.randint(0, 5)
if num == 1:
    print("Absolutely not")
elif num == 2:
    print("Definitely")
elif num == 3:
    print("It is decidedly so")
elif num == 4:
    print("no.")
else:
    print("i guess")
copyright()