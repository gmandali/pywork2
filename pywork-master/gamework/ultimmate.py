from colorama import Fore, Style
print(Fore.LIGHTBLUE_EX, Style.BRIGHT, '''
░██████╗░░█████╗░██╗░░░██╗██████╗░░█████╗░██╗░░░██╗██╗░██████╗
██╔════╝░██╔══██╗██║░░░██║██╔══██╗██╔══██╗██║░░░██║╚█║██╔════╝
██║░░██╗░███████║██║░░░██║██████╔╝███████║╚██╗░██╔╝░╚╝╚█████╗░
██║░░╚██╗██╔══██║██║░░░██║██╔══██╗██╔══██║░╚████╔╝░░░░░╚═══██╗
╚██████╔╝██║░░██║╚██████╔╝██║░░██║██║░░██║░░╚██╔╝░░░░░██████╔╝
░╚═════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░░╚═════╝░

░█████╗░██████╗░███████╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
██║░░╚═╝██████╔╝█████╗░░███████║░░░██║░░░██║██║░░██║██╔██╗██║
██║░░██╗██╔══██╗██╔══╝░░██╔══██║░░░██║░░░██║██║░░██║██║╚████║
╚█████╔╝██║░░██║███████╗██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝''')
start = ""
while start != "/quit":
    start = input("What would you like to use today(/help for list): ").lower()
    if start == "/help":
        print(Fore.LIGHTGREEN_EX, Style.BRIGHT, """
calc - calculator
cir calc - circle calculator
herogame - hero game
emailslice - email slicer
quit - to quit
visual - for visual mode
security - for a free wireless security website""")

    elif start == "calc":

        print(Fore.LIGHTGREEN_EX, Style.BRIGHT, "Hello! I am calculator 3.0")
        print(Fore.LIGHTGREEN_EX, Style.BRIGHT, " I am a calculator made by Gaurav")
        print(Fore.LIGHTGREEN_EX, Style.BRIGHT, "use % for modula")
        print(Fore.LIGHTGREEN_EX, Style.BRIGHT, "use * for multiplication")
        print(Fore.LIGHTGREEN_EX, Style.BRIGHT, "use ** for exponent")
        print(Fore.LIGHTGREEN_EX, Style.BRIGHT, "use - for subtraction")
        print(Fore.LIGHTGREEN_EX, Style.BRIGHT, "use + for addition")
        try:

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
        except ValueError:
            print('wrong type')
        else:
            print("Invalid operation")
            print("Pls restart program " + user)
        print("""Your hero is in danger.
        he is surrounded by evil trolls.
        this is his last battle.""")
        hero = int(input("Enter a number divisible by 3: "))
        troll = 0
        damage = 3
        while hero != 0:
            print("your hero swung and defeated one troll but took 3 damage points.")
            troll += 1
            hero -= 3
        print(Fore.LIGHTRED_EX, Style.BRIGHT, "your hero fought valiantly and defeated", troll,
              "trolls but is no more.")

    elif start == "cir calc":
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
        start = input("What would you like to use today(/help for list): ").lower()
    elif start == "emailslice":
        email_id = input("Enter your email id: ").strip()

        username = email_id[:email_id.index('@')]

        domain = email_id[email_id.index('@') + 1:]

        print(f"Your username :{username} and your domain name is {domain}")
    elif start == "visual":
        from tkinter import *
        from tkinter import messagebox

        root = Tk()


        def popup():
            messagebox.showerror('wrong', 'This is the wrong door >:(')


        def correct():
            messagebox.showinfo('correct', 'this is the correct door :)')


        def three():
            cald = Toplevel()
            cool = Toplevel()
            nand = Toplevel()
            Button(cool, text='Click the correct door to win the game', pady=100, padx=20,
                   command=popup).pack()
            Button(cald, text='Click the correct door to win the game', pady=100, padx=20,
                   command=correct).pack()
            Button(nand, text='Click the correct door to win the game', pady=100, padx=20,
                   command=popup).pack()


        def two():
            cald = Toplevel()
            cool = Toplevel()
            Button(cool, text='Click the correct door to win the game', pady=100, padx=20,
                   command=popup).pack()
            Button(cald, text='Click the correct door to win the game', pady=100, padx=20,
                   command=correct).pack()


        def myclick():
            tki = Toplevel()
            Button(tki, text='do you want two doors', command=two,relief=SUNKEN).pack()
            Button(tki, text='do you want three doors', command=three,relief=SUNKEN).pack()


        def clickbait():
            messagebox.showwarning('HACKED', 'OH NO, YOU ARE HACKED >:)')


        def clickedddd():
            tki = Toplevel()
            Button(tki, text='YOU WON THE LOTTERY SO CLICK TO GET YOUR PRIZE', command=clickbait).pack()


        button1 = Button(root, text='click to play door_game 2.0', command=myclick).pack()
        button2 = Button(root, text='click here to see a visual advertisement', command=clickedddd).pack()

        mainloop()

    elif start == "security":

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
                print("Wassup G, you are", mood)
                print("security is ", security)
                print("password and username to your account is Gaurav and Rubik")
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
                print("Wassup Baby, I heard that you are", mood)
                print("security is", security)
                print("password and username to your account is Priya and Pink Dress")
                command = input("Would you like to upgrade?(Yes or No): ")
                if command == "Yes":
                    coins -= 1000
                    security += 1
                    print("you have", coins, "coins and security is", security)
                elif command == "No":
                    print(Fore.GREEN, Style.BRIGHT, "ok")
                else:
                    print(Fore.RED, Style.BRIGHT, "illegal response.")
            else:
                print(Fore.RED, Style.BRIGHT, "access denied try again. :(")
        else:
            print(Fore.RED, Style.BRIGHT, "invalid login.")
    elif start == "quit":
        break

    else:
        print(Fore.RED, Style.BRIGHT, "I can't find that in my item list. :(")
print(Fore.CYAN, Style.BRIGHT, "ok, Have a good day")
copyright()
