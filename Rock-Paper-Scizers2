"""
We are about to play rock paper scizers with the computer
1 is for the rock
0 is for the paper
    and 
-1 is for the scizers
"""
import random

print("Let's play Rock-Paper-Scizers")
print("Here make your choice: ")
print('''For Rock press r.\nFor Papers press p.\nFor Scizers press s.''')

your_choice = input("Enter your choice: ")                  #User enters his/her choice

dict = {"r" : 1, "p" : 0, "s": -1}                          #This dictionary assigns your string value to the respective number
you = dict[your_choice]
reversed_dict = {1 : "Rock", 0 : "Paper", -1 : "Scizers"}   #This dictionary is only used for the output purpose only

computer = random.choice(list(reversed_dict.keys()))        #This line allows the computer to randomly pick an integer key (variable) from the reversed_dict

print(f"You have chosen:\t{reversed_dict[you]}\nComputer has chosen:\t{reversed_dict[computer]}")


if(you == computer):
    print("It's a draw.")

else:
    if((computer - you) == -1 or (computer - you) == 2):
        print("You have lost the match")

    elif((computer - you) == 1 or (computer - you) == -2):
        print("You have won the match!")

    else:
        print("There might have been an error!")

print("Let's play again. Shall we?")


# Well the above logic is described below:-

#     if(you == 1 and computer == -1): (computer - you) = -2
#         print("You Win!")

#     elif(you == 1 and computer == 0): (computer - you) = -1
#         print("You have lost!")

#     elif(you == 0 and computer == -1): (computer - you) = -1
#         print("You have lost!")

#     elif(you == 0 and computer == 1): (computer - you) = 1
#         print("You Win!")

#     elif(you == -1 and computer == 1): (computer - you) = 2
#         print("You have lost!")

#     elif(you == -1 and computer == 0): (computer - you) = 1
#         print("You Win!")

