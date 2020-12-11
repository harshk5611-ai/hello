import random
print("Welcome to the snake, water, gun game ..." + '''
Enter 's' to choose snake , 'w' for water and 'g' for gun .\n''')
lst = ("snake", "water", "gun")
chances = 1
compoints = 0
userpoints = 0
while chances < 11:
    comchoice = random.choice(lst)
    userchoice = input("Enter Your Choice here : \n").lower()
    if userchoice == "s"and comchoice == "gun":
        print(f"The computer chose {comchoice} and You Lose")
        compoints = compoints + 1
    elif userchoice == "s"and comchoice == "water":
        print(f"The computer chose {comchoice} and You Won ! :)")
        userpoints = userpoints+1
    elif userchoice == "w"and comchoice == "gun":
        print(f"The computer chose {comchoice} and You Won ! :)")
        userpoints = userpoints + 1
    elif userchoice == "w" and comchoice == "snake":
        print(f"The computer chose {comchoice} and You Lose")
        compoints = compoints + 1
    elif userchoice == "g"and comchoice == "water":
        print(f"The computer chose {comchoice} and You Lose")
        compoints = compoints + 1
    elif userchoice == "g"and comchoice == "snake":
        print(f"The computer chose {comchoice} and You Won ! :)")
        userpoints = userpoints + 1
    elif userchoice == "w"and comchoice == "water":
        print(f"The computer also Chose {comchoice} and this round tied . !!")
    elif userchoice == "g"and comchoice == "gun":
        print(f"The computer also Chose {comchoice} and this round tied . !!")
    elif userchoice == "s"and comchoice == "snake":
        print(f"The computer also Chose {comchoice} and this round tied . !!")
    else:
        print("Wrong Input :/   !")
        continue
    print(f"There are {10 - chances} rounds left.")
    print(f"Computer's points = {compoints} and Your Points = {userpoints}")
    chances = chances + 1
if compoints > userpoints:
    print(f"The computer won with {compoints - userpoints} more points :/ !")
elif userpoints > compoints:
    print(f"You won with {userpoints - compoints} more points :) !")
else:
    print(f"The game tied with {compoints} - {userpoints} !! ")
