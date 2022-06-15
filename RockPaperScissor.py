# MODS
import random

print("--------------------------------------")
print("-- WELCOME TO A GAME OF TIC TAC TOE --")
print("--------------------------------------")
print("\t\t\t\t  press (q) to quit")
print("\t\t\t\t\t\t lets begin...\n\n")

# Global variables
win = 0
loss = 0
tie = 0

# MAIN
while True:
    options = ["rock", "paper", "scissor"]
    cpu_choice = random.choice(options)

    user_choice = input("Pick rock, paper, or scissors: ").lower()

    # Check for a tie
    if user_choice == cpu_choice:
        print(f"ITS A TIE! You both picked [{user_choice}].\n")
        tie += 1

    # If the user picks rock
    elif user_choice == "rock":
        if cpu_choice == "scissor":
            print(f"YOU WIN! You smashed computer's [{cpu_choice}].\n")
            win += 1
        elif cpu_choice == "paper":
            print(f"YOU LOSE! Computer caught you with [{cpu_choice}].\n")
            loss += 1

    # If the user picks paper
    elif user_choice == "paper":
        if cpu_choice == "rock":
            print(f"YOU WIN! You caught computer's [{cpu_choice}].\n")
            win += 1
        elif cpu_choice == "scissor":
            print(f"YOU LOSE! Computer cut you with [{cpu_choice}].\n")
            loss += 1

    # If the user picks scissor
    elif user_choice == "scissor":
        if cpu_choice == "paper":
            print(f"YOU WIN! You cut up computer's [{cpu_choice}].\n")
            win += 1
        elif cpu_choice == "rock":
            print(f"YOU LOSE! Computer smashed you with [{cpu_choice}].\n")
            loss += 1

    # If the user quits the game
    elif user_choice == "q":
        total = (win + loss + tie)
        print(f"\n\n\t\t\t [{total}]GAMES")
        print(f"\t\tWIN:{win} LOSS:{loss} TIE:{tie}")
        break
