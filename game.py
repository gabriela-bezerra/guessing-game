"""A number-guessing game."""

import random


def guessing_game():
    print()
    print("Welcome to the guessing game!")
    print()
    name = input("What is your name? ")

    print()

    range1 = int(input(" Choose a start range > "))
    range2 = int(input(" Choose an end range > "))

    pc_number = random.randint(range1, range2)

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
            break
            print()

        elif guessed_number < pc_number:
            print("Your guess was too low, try again.")
            tries = tries + 1
            if tries > 5:
                print(" Too many tries!")
                play_again = input(
                    "Would you like to play again? Y/N  > ").lower()

                if play_again == "y":
                    guessing_game()
                else:
                    print("See you next time!")
                    break
            print()

        elif guessed_number > pc_number:
            print("Your guess was too high, try again.")
            tries = tries + 1
            if tries > 5:
                print(" Too many tries!")
                play_again = input(
                    "Would you like to play again? Y/N  > ").lower()

                if play_again == "y":
                    guessing_game()
                else:
                    print("See you next time!")
                    break
            print()

        else:
            print(" Number not valid, try again.")
            print()


guessing_game()
