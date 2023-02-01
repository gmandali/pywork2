
print("Hello! I am calculator/translator/email slicer 3.0")
print(" I am made by Gaurav")
print("Use c to use it and type anything else to use the secret code translator and email for the email slicer app")
print("use % for modula")
print("use * for multiplication")
print("use ** for exponent")
print("use - for subtraction")
print("use + for addition")
user = input("Enter your name: ")
what = input("Enter what is your buisness here:")
if what == "c":
    op = input("Enter a operation: ")
    if op in "*,/,**,%,+,-":
        print("Enter next info " + user)
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if op == "+":
            print(num1 + num2)
            print("thank you for using calculator 3.0 " + user)
        elif op == "-":
            print(num1 - num2)
            print("thank you for using calculator 3.0 " + user)
        elif op == "*":
            print(num1 * num2)
            print("thank you for using calculator 3.0 " + user)
        elif op == "/":
            print(num1 / num2)
            print("thank you for using calculator 3.0 " + user)
        elif op == "**":
            print(num1 ** num2)
            print("thank you for using calculator 3.0 " + user)
        else:
            print(num1 % num2)
    else:
        print("Invalid operation")
        print("Pls restart program " + user)
elif what == "email":
    email_id = input("Enter your email id:").strip()

    username = email_id[:email_id.index('@')]

    domain = email_id[email_id.index('@') + 1:]

    print(f"Your username :{username} and your domain name is {domain}")
else:
    def translate(phrase):
        translation = ""
        for letter in phrase:
            if letter in "AEIOUaeiou":
                translation = translation + "@#$%^&*("
            else:
                translation = translation + letter
        return translation


    print(translate(input("Enter a phrase: ")))