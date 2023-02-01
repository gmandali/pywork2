print('''Peter has 45 pumpkins. 
He goes to the market and buys x more. 
He has 70 now.
How many did he buy?''')
answer = int(input("What is the answer to the problem above?: "))

print('''


He divides all apples evenly among 9 friends.
 there are 4.5 apples
 How many apples did Tom give to each of his friends? 
 There are 9 friends of seats on the bus.
To find how many apples Tom gave to each of his friends, divide the total number of apples by the number of friends.''')
answer_two = float(input("What is the answer to this problem?: "))
if answer == 25 and answer_two == 0.5:
    print(" You got 100% correct.")
elif answer == 25 and answer_two != 0.5:
    print("you got 50% correct.")
    print("You got number 2 wrong.")
    print("correct answer is 0.5")
elif answer != 25 and answer_two == 0.5:
    print("You got 50% correct.")
    print("You got number one wrong.")
    print('Correct answer is 25')
else:
    print("You got 0% correct. :(")
