import sys


def display_menu():
    menu_items = [
        "[ 1 ] Addition ( + )",
        "[ 2 ] Subtraction ( - )",
        "[ 3 ] Multiplication ( * )",
        "[ 4 ] Division ( / )",
        "[ 5 ] Modulus ( % )",
        "[ x ] Quit ( Close application )"
    ]

    print("Please select an operation from the following menu:\n")

    for item in menu_items:
        print(item)  # Display selection menu

    get_selection()  # Get user selection


def get_selection():
    selection = input()  # User selection

    if selection == "1":
        print("You've selected Addition!\n")
    elif selection == "2":
        print("You've selected Subtraction!\n")
    elif selection == "3":
        print("You've selected Multiplication!\n")
    elif selection == "4":
        print("You've selected Division!\n")
    elif selection == "5":
        print("You've selected Modulus!\n")
    elif selection.lower() == "x":
        print("Goodbye!")
        sys.exit()  # Quit application
    else:
        print("Sorry, that is not a valid selection.\n\n")
        display_menu()  # Return to selection menu

    get_user_input(selection)  # Get user input


def get_user_input(selection):
    integer_list = []  # Initialize empty list for integers

    print("For this operation, please input two integers.\n")  # Print directions

    print("First integer: ")
    integer_list.append(int(input()))  # Add first integer to integers_list

    print("Second integer: ")
    integer_list.append(int(input()))  # Add second integer to integers_list

    run_operation(selection, integer_list)  # Run selected operation on integers


def run_operation(selection, integers_list):
    x = integers_list[0]
    y = integers_list[1]

    # Corrected in Week 3 Discussion by implementing a try/except statement to handle ZeroDivisionError

    """
    if selection == "1":
        print("\n\n", x, "plus", y, "equals", x + y)  # Add x and y
    elif selection == "2":
        print("\n\n", x, "minus", y, "equals", x - y)  # Subtract x and y
    elif selection == "3":
        print("\n\n", x, "multiplied by", y, "equals", x * y)  # Multiply x and y
    elif selection == "4":
        if y == 0:  # Check for divide by zero
            print("Error: You can't divide by 0. Please try again.")
            display_menu()
        else:
            print("\n\n", x, "divided by", y, "equals", x / y)  # Divide x and y
    elif selection == "5":
        print("\n\n", x, "modulus", y, "equals", x % y)  # Modulus x and y
    else:
        print("\n\n", "Sorry, this application has experienced an error.")
        sys.exit()  # Quit application
    """

    try:
        if selection == "1":
            print("\n\n", x, "plus", y, "equals", x + y)  # Add x and y
        elif selection == "2":
            print("\n\n", x, "minus", y, "equals", x - y)  # Subtract x and y
        elif selection == "3":
            print("\n\n", x, "multiplied by", y, "equals", x * y)  # Multiply x and y
        elif selection == "4":
            print("\n\n", x, "divided by", y, "equals", x / y)  # Divide x and y
        elif selection == "5":
            print("\n\n", x, "modulus", y, "equals", x % y)  # Modulus x and y
        else:
            print("\n\n", "Sorry, this application has experienced an error.")
            sys.exit()  # Quit application
    except ZeroDivisionError as e:
        print(str(e) + "<-- We caught this error!")  # Now we can print a helpful message to guide the user
        print("\nYou will be returned to the menu to try again.\n")  # <-- Helpful message
        display_menu()  # Return to selection menu

    # TODO: Error handling for mathematical operations and non-compliant user input (COMPLETED)


if __name__ == "__main__":
    display_menu()
