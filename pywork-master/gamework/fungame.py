
security = 0
coins = 2000

username = ""
while not username:
    username = input("Username: ")
password = ""
while not password:
    password = input("Password: ")
if username == "Gaurav" and password == "Rubik":
    special_question = ""
    while not special_question:
        special_question = str(input("What is your favorite color?: "))
    special_question_two = ""
    while not special_question_two:
        special_question_two = str(input("What is your method for pyraminx?: "))
    if special_question == "Orange" and special_question_two == "l4e":
        security = 10
        print("You are in.")
        coins = 30000
        mood = input("How are you?: ")
        print("Wassup G, you are",mood)
        print("security is ",security)
        print("password and username to your account is Gaurav and Rubik")
        command = input("Would you like to upgrade?(Yes or No): ")
        if command == "Yes":
            coins -= 1000
            security += 1
            print("you have",coins,"coins")
        elif command == "No":
            print("ok")
        else:
            print("illegal response.")
    else:
        print("access denied try again. :(")
elif username == "Vidip" and password == "Roblox":
    print("yo vidkid.")
    security = 5
    print("security is ", security)
    coins = 2000
    command = input("Would you like to upgrade?(Yes or No): ")
    if command == "Yes":
        coins -= 1000
        security += 1
        print("you have", coins, "coins")
    elif command == "No":
        print("ok")
    else:
        print("illegal response.")
elif username == "Priya" and password == "Pink Dress":

    special_question = ""
    while not special_question:
        special_question = str(input("What is your favorite color?: "))
    special_question_two = ""
    while not special_question_two:
        special_question_two = str(input("What is your favorite food?: "))
    if special_question == "Pink" and "Fried Corn":
        security = 10
        print("You are in.")
        coins = 10000
        mood = input("How are you?: ")
        print("Wassup Baby, you are", mood)
        print("security is", security)
        print("password and username to your account is Priya and Pink Dress")
        command = input("Would you like to upgrade?(Yes or No): ")
        if command == "Yes":
            coins -= 1000
            security += 1
            print("you have", coins, "coins")
        elif command == "No":
            print("ok")
        else:
            print("illegal response.")
    else:
        print("access denied try again. :(")
else:
    print("invalid login.")