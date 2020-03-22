import sys
from random import randint


def display_menu():
    menu_items = [
        "[ 1 ] Generate 3-digit lottery number",
        "[ 2 ] Generate 4-digit lottery number",
        "[ x ] Quit (Exit application)"
    ]

    print("Please select an option from the following menu:\n")  # Print directions

    for item in menu_items:
        print(item)  # Display selection menu

    get_user_selection()  # Get user input


def get_user_selection():
    lottery_number = 0
    selection = input()  # User input

    while selection.lower() != "x":
        if selection == "1":
            print("Generating 3-digit lottery number...")
            lottery_number = pull_lever(3)  # Generate random 3-digit lottery number
        elif selection == "2":
            print("Generating 4-digit lottery number...")
            lottery_number = pull_lever(4)  # Generate random 4-digit lottery number
        else:
            print("Please make a selection from the following menu by entering '1' or '2' in your terminal.")
            display_menu()  # Return to selection menu

        print("Your random", selection, "-digit lottery number is", lottery_number)  # Print random lottery number

        display_menu()  # Return to selection menu

    exit_game()


def pull_lever(digits):
    range_start = 10 ** (digits - 1)  # Define length of random integer
    range_end = (10 ** digits) - 1

    return randint(range_start, range_end)  # Returns random 3/4-digit integer


def exit_game():
    print("Thank for playing, and always gamble responsibly! Goodbye!")

    sys.exit()  # Exit application


if __name__ == "__main__":
    print("You're playing the Pick-3, Pick-4 Lottery Generator!\n\n")
    display_menu()
