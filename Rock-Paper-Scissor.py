import sys
import random

print("")

title = """ **********ABOUT THE GAME********\n

A classic two-person game. Players start each round by saying, “rock, paper, scissors, shoot!” On “shoot,” each player holds out their fist for rock, flat hand for paper, or their index and middle finger for scissors. Rock crushes scissors, scissors cut paper, and paper covers rock. See who wins each round!

"""
print(title)
print("")
playerchoice = input(
    "👾Enter.... \n1 for Rock🪨 \n2 for Paper📃 OR \n3 for Scissors✂️:\n\n"
)

player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit(
        """ Try Again!
             
        
        ....You must enter 1, 2, 3.
"""
    )
    print(input("👾Enter.... \n1 for Rock🪨 \n2 for Paper📃 OR \n3 for Scissors✂️:\n\n"))


computerchoice = random.choice("123")


computer = int(computerchoice)

print("")

print("you chose " + playerchoice + ".")
print("Computer chose " + computerchoice + ".")
print("")

if player == computer:
    print("I'ts a tie🤐!")
elif player == 1 and computer == 3:
    print("You win😎!")
elif player == 2 and computer == 1:
    print("You win😎!")
elif player == 3 and computer == 2:
    print("You win😎!")
else:
    print("You loose😒, n\ 🐍 wins!")
