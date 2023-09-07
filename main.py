import random

while True:
    choises = ["paper", "scissors", "rock"]

    computer = random.choice(choises)
    player = None

    while player not in choises:
        player = input("rock, scissor or paper?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("You tie!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    repit = input("Do you wanna play again?: (yes/no)").lower()

    if repit != "yes":
        break

print("Bye")