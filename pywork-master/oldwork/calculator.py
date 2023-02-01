


print("Hello! I am calculator 3.0")
print(" I am a calculator made by Gaurav")
print("use % for modula")
print("use * for multiplication")
print("use ** for exponent")
print("use - for subtraction")
print("use + for addition")

op = input("Enter a operation: ")
user = input("Enter your name: ")
if op in "*,/,**,%,+,-":
    print("Enter next info " + user)
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if op == "+":
        print(num1 + num2)
        print("thank you for using calculator 3.0")
    elif op == "-":
        print(num1 - num2)
        print("thank you for using calculator 3.0")
    elif op == "*":
        print(num1 * num2)
        print("thank you for using calculator 3.0")
    elif op == "/":
        print(num1 / num2)
        print("thank you for using calculator 3.0")
    elif op == "**":
        print(num1 ** num2)
        print("thank you for using calculator 3.0")
    else:
        print(num1 % num2)
else:
    print("Invalid operation")
    print("Pls restart program " + user)
