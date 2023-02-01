
command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start" :
        print("car started...")
    elif command == "stop":
        print("car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the car""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that.")