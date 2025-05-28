# Q2> The game() function in a program let's thee user to play the game and return the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random

def game():
    print("The game we are about to play is Rock-Paper-Scissors")

    score = 0  # Initialize score

    try:
        with open("hiscore.txt", "r") as f:
            hiscore = f.read()
            if (hiscore.strip().isdigit()):
                hiscore = int(hiscore)
            else:
                hiscore = 0
    except FileNotFoundError:  # If file doesn't exist, set high score to 0
        hiscore = 0
    score = 0
    breaking_point = 1
    while(breaking_point != 0 ):
        print("\nHere, make your choice: ")
        print('''For Rock press r.\nFor Paper press p.\nFor Scissors press s.''')

        your_choice = input("Enter your choice (or press 'q' to quit): ").lower()

        if(your_choice == 'q'):  # If the user wishes to quit he can press 'q'
            print("Thanks for playing! Exiting game...")
            break

        dict = {"r": 1, "p": 0, "s": -1}

        if(your_choice not in dict):  # If the user's choice is not present in the dictionary
            print("Invalid choice! Please enter 'r', 'p', or 's'.")
            continue

        you = dict[your_choice]
        reversed_dict = {1: "Rock", 0: "Paper", -1: "Scissors"}   # Assigning numbers to the user's choice

        computer = random.choice(list(reversed_dict.keys()))  # Allowing the computer to take his own value 

        print(f"You have chosen:\t{reversed_dict[you]}\nComputer has chosen:\t{reversed_dict[computer]}")

        if(you == computer):
            print("It's a draw.")

        elif((computer - you) == -1 or (computer - you) == 2):
            print("You have lost the match")
            breaking_point = 0  # score = 0 when the user looses

        elif((computer - you) == 1 or (computer - you) == -2):
            print("You have won the match!")
            score += 1  # Increase score if user wins


        print(f"Your current score: {score}")
        with open('highscore.txt','r') as f:
            r = f.readline()
            sc = int(r)
        if(score > sc):
            hiscore = score
            with open("highscore.txt", "w") as f:
                f.write(str(hiscore))
            print("New high score!")

    print("\n \n")
    print(f"Your final score was: {score}")
    print(f"The highest score recorded: {sc}")

print("Ready to play the game")
game()
