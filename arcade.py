import sys
from guess_number import guess_number
from rps_args_8 import rps


def play_game(name="Player One"):

    welcome_back = False

    while True:

        if welcome_back == True:
            print(f"\nHi {name}, welcome back to the Arcade menu.")
        else:
            print(f"\nHi {name}, welcome to the Arcade menu.")

        playerchoice = input(
            "\nPlease choose a game!!!\n\t1 = 'Rock, Paper, Scissors'\n\t2 = 'Guess My Number'\nPress 'X' to exit the arcade.\n")

        if playerchoice.lower() not in ["1", "2", "x"]:
            print(f"\n{name}, please enter1, 2 or X.")
            return play_game(name)

        welcome_back = True

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_my_number = guess_number(name)
            guess_my_number()
        else:
            print("\nSee you next time.\n")
            sys.exit(f"Bye {args.name}! 👋\n")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    play_game(args.name)
