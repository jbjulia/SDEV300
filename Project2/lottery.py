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
    selection = input("\n")  # User input

    while selection.lower() != "x":
        if selection == "1":
            print("\nGenerating 3-digit lottery number...")
            lottery_number = pull_lever(3)  # Generate random 3-digit lottery number
        elif selection == "2":
            print("\nGenerating 4-digit lottery number...")
            lottery_number = pull_lever(4)  # Generate random 4-digit lottery number
        else:
            print("\nPlease make a selection from the following menu by entering '1', '2' or 'x' in your terminal.\n")
            display_menu()  # Return to selection menu

        print("\nYour random",
              len(str(lottery_number)),  # Get length of lottery number
              "-digit lottery number is: ",
              lottery_number,
              "\n")  # Print random lottery number

        display_menu()  # Return to selection menu

    exit_game()  # Exit game


def pull_lever(digits):
    range_start = 10 ** (digits - 1)  # Define length of random integer
    range_end = (10 ** digits) - 1

    return randint(range_start, range_end)  # Returns random 3/4-digit integer


def exit_game():
    print("\nThank for playing, and always gamble responsibly! Goodbye!")

    sys.exit()  # Exit application


if __name__ == "__main__":
    print("You're playing the Pick-3, Pick-4 Lottery Generator!\n\n")
    display_menu()
