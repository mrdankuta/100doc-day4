import random

rpcOptions = ["Rock","Paper","Scissors"]

numberOfChoices = len(rpcOptions)

randomChoiceIndex = random.randint(0, numberOfChoices - 1)

pcChoice = rpcOptions[randomChoiceIndex]

playerInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

if playerInput >= 0 and playerInput <= 2:
    playerChoice = rpcOptions[playerInput]
    print(f"You chose {playerChoice}. \nComputer chose {pcChoice} ")
    
    if playerInput == 0 and randomChoiceIndex != 0:
        if randomChoiceIndex == 1:
            print("You Lose. Game Over!")
        else:
            print("You Win! Congratulations.")
    elif playerInput == 1 and randomChoiceIndex != 1:
        if randomChoiceIndex == 2:
            print("You Lose. Game Over!")
        else:
            print("You Win! Congratulations.")
    elif playerInput == 2 and randomChoiceIndex != 2:
        if randomChoiceIndex == 0:
            print("You Lose. Game Over!")
        else:
            print("You Win! Congratulations.")
    else:
        print("It's a draw. Play again!")
else:
    print("You entered an invalid number. You Lose!")
    

