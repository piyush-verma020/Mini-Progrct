import random

def game():
    print("The game we are about to play is Rock-Paper-Scissors")

    score = 0  # Initialize score

    try:
        with open("highscore.txt", "r") as f:
            hiscore = f.read()
            if (hiscore.strip().isdigit()):
                hiscore = int(hiscore)
            else:
                hiscore = 0

        breaking_point = 1
        while breaking_point != 0:
            print("\nHere, make your choice: ")
            print('''For Rock press r.\nFor Paper press p.\nFor Scissors press s.''')

            your_choice = input("Enter your choice (or press 'q' to quit): ").lower()

            if your_choice == 'q':
                print("Thanks for playing! Exiting game...")
                break

            dict = {"r": 1, "p": 0, "s": -1}

            if your_choice not in dict:
                print("Invalid choice! Please enter 'r', 'p', or 's'.")
                continue

            you = dict[your_choice]
            reversed_dict = {1: "Rock", 0: "Paper", -1: "Scissors"}
            computer = random.choice(list(reversed_dict.keys()))

            print(f"You have chosen:\t{reversed_dict[you]}\nComputer has chosen:\t{reversed_dict[computer]}")

            if you == computer:
                print("It's a draw.")
            elif (computer - you == -1 or computer - you == 2):
                print("You have lost the match")
                breaking_point = 0
            elif (computer - you == 1 or computer - you == -2):
                print("You have won the match!")
                score += 1  # Corrected line

            print(f"Your current score: {score}")

            if score > hiscore:
                hiscore = score
                with open("highscore.txt", "w") as f:
                    f.write(str(hiscore))
                print("New high score!")

        print("\n\n")
        print(f"Your final score was: {score}")
        print(f"The highest score recorded: {hiscore}")

    except FileNotFoundError:
        print("High score file not found, starting with high score = 0.")
        hiscore = 0

print("Ready to play the game")
game()
