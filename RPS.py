import random

choice = ["rock", "paper", "scissor"]

user = None
p=0
c=0
while user not in choice:

    if user == "quit":
        print("player:", p)
        print('computer:', c)
        break
    print("#---------enter 'quit' to quit the game------------")
    while user != "quit":
        computer = random.choice(choice)
        user = input('"rock", "paper", "scissor"?')
        print()
        print("Player: ", user)
        print("Computer: ", computer)

        if computer == user:
            print("Tie!!")
        elif computer == "rock":
            if user == "paper":
                print("You win!")
                p+=1
            elif user == "scissor":
                print("You lose!")
                c+=1
        elif computer == "paper":
            if user == "scissor":
                print("You win!")
                p += 1
            elif user == "rock":
                print("You lose!")
                c += 1
        elif computer == "scissor":
            if user == "rock":
                print("You win!")
                p += 1
            elif user == "paper":
                print("You lose!")
                c += 1
        print()

