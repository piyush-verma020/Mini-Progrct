# Write a program that  generates a random number and asks user to guess it.
# If the player's guess is higher than the actual number, the program displays "Lower number please". Similarly if the user guesses
# it lower, the program prints "Higher number please". When the programer or the user gueses the number correctly, the program will 
# displays the number of guesses the player used to arrive at the number

import random
import time
import sys

ch = 0
computer = random.randint(1,10)
ch1 = 1 
ch1 = int(input("Are you ready for the game if yes press 1 or else press 0: "))
while(ch1 != 0):
    print("\n")
    user_choice = int(input("Guess the number dear user between 1 and 10: "))
    if (ch > 10):
        print("It's enough bro!")
        print(f"You took {ch} guesses!")
        print("How could you be so bad to guesing")
        print("I am deleting your windows 11")
        for i in range(10):  # Repeat 10 times
            for dots in ['.', '..', '...']:
                print(f'\rLoading{dots}   ', end='')
                time.sleep(0.5)
        print("\n")
        print("Just kidding bro!")
        print("You can try again later :)")
        break
    elif(user_choice < computer):
        print("Higher number please!")
        ch += 1
    elif(user_choice > computer):
        print("Lower number please!")
        ch += 1
    elif(user_choice == computer):
        print(f"You got the numbner which was {computer} and the numnber of guesses you took was {ch}")
        try:
            with open("no_of_guess.txt", "r") as f:
                r = f.readline().strip()
                r = int(r)
        except (ValueError, FileNotFoundError):
            r = 1000

        if(ch < r):
            with open("no_of_guess.txt", "w") as f:
                f.write(str(ch))
        break
    else:
        print("COMPUTATION ERROR!!")
