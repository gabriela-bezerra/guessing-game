"""A number-guessing game."""

import random


def guessing_game():
    print()
    print("Hi")
    print()
    name = input("What is your name? ")

    print(f"Welcome {name} to the guessing game!")
    print()
    print("I'm thiking of a number between 1 an 100")

    pc_number = random.randint(1, 100)

    tries = 0

    while True:
        guessed_number = int(input(" Try to guess my number > "))

        if guessed_number == pc_number:
            print(
                f"Congratulations {name}, you found my number in {tries} tries")
            print()

            play_again = input("Would you like to play again? Y/N  > ").lower()

            if play_again == "y":
                guessing_game()
            else:
                print("See you next time!")
            break
            print()

        elif guessed_number < pc_number:
            print("Your guess was too low, try again.")
            tries = tries + 1
            print()
        elif guessed_number > pc_number:
            print("Your guess was too high, try again.")
            tries = tries + 1
            print()
        else:
            print(" Number not valid, try again.")
            print()


guessing_game()
