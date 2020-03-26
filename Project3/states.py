import sys

import state_data


def display_menu():
    menu_items = [
        "[ 1 ] Display all States and their data",
        "[ 2 ] Query a specific state",
        "[ 3 ] Update state data",
        "[ 4 ] Quit (Exit program)"
    ]

    print("Please make a selection from the following menu:\n")

    for item in menu_items:
        print(item)  # Print selection menu

    selection = int(input("\n"))  # Get user's selection

    try:
        if selection == 1:
            display_all_state_data()
        elif selection == 2:
            query_specific_state()
        elif selection == 3:
            update_state_data()
        elif selection == 4:
            exit_program()
        else:
            print("\nSorry, please try again.\n\n")
    except ValueError:
        print("\nPlease select an option from the menu by typing either '1', '2', 3' or '4'.\n\n")
        display_menu()  # Display selection menu


def display_all_state_data():
    capitol = ""
    bird = ""
    flower = ""

    try:
        for state in state_data.states:
            for key in state.keys():
                if key != "state":
                    for item in state.values():
                        capitol = item[0]
                        bird = item[1]
                        flower = item[2]
                    print("State: ", key.title(),
                          "\n\tCapitol: ", capitol.title(),
                          "\n\tBird: ", bird.title(),
                          "\n\tFlower: ", flower.title(),
                          "\n"
                          )
    except ImportError:
        print("\nError: Could not import state data.")
        sys.exit()  # Exit program

    input("\nPress any key to return to the selection menu...\n\n")  # Wait for user input

    display_menu()  # Display selection menu


def query_specific_state():
    state_found = False
    capitol = ""
    bird = ""
    flower = ""
    user_input = input("\nPlease enter the name of the state you wish to query: ").lower()  # Get user input

    try:
        for state in state_data.states:
            for key in state.keys():
                if key == user_input:
                    for item in state.values():
                        capitol = item[0]
                        bird = item[1]
                        flower = item[2]
                    print("\nState: ", key.title(),
                          "\n\tCapitol: ", capitol.title(),
                          "\n\tBird: ", bird.title(),
                          "\n\tFlower: ", flower.title(),
                          "\n"
                          )
                    state_found = True
                    display_menu()
                else:
                    pass
    except (ImportError, KeyboardInterrupt):
        print("\nError: Could not import state data.")
        sys.exit()

    if not state_found:
        print("\nSorry, that state could not be found.\n")

    input("\nPress any key to return to the selection menu...\n\n")

    display_menu()


def update_state_data():
    state_found = False
    capitol = ""
    bird = ""
    flower = ""
    user_input = input("\nPlease enter the name of the state you wish to update: ").lower()  # Get user input

    try:
        for state in state_data.states:
            for key in state.keys():
                if key == user_input:
                    for item in state.values():
                        capitol = item[0]
                        bird = item[1]
                        flower = item[2]
                    print("\nState: ", key.title(),
                          "\n\tCapitol: ", capitol.title(),
                          "\n\tBird: ", bird.title(),
                          "\n\tFlower: ", flower.title(),
                          "\n"
                          )
                    state_found = True
                    element = input("Which element do you wish to update? ('capitol', 'bird', 'flower'): ")
                    if element == "capitol":
                        item[0] = input(
                            "\nPlease enter a new state capitol: ")  # TODO: Function to make changes permanent
                        print("\nYou have successfully updated the state capitol of", key.title(), "to: ",
                              item[0].title() + ".")
                    elif element == "bird":
                        item[1] = input(
                            "\nPlease enter a new state bird: ")  # TODO: Function to make changes permanent
                        print("\nYou have successfully updated the state bird of", key.title(), "to: ",
                              item[1].title() + ".")
                    elif element == "flower":
                        item[2] = input(
                            "\nPlease enter a new state flower: ")  # TODO: Function to make changes permanent
                        print("\nYou have successfully updated the state flower of", key.title(), "to: ",
                              item[2].title() + ".")
                    else:
                        print("\nSorry, that element does not exist, please try again.\n")
                        display_menu()
                else:
                    pass
    except (ImportError, KeyboardInterrupt):
        print("\nError: Could not import state data.")
        sys.exit()

    if not state_found:
        print("\nSorry, that state could not be found.\n")

    input("\nPress any key to return to the selection menu...\n\n")

    display_menu()


def exit_program():
    print("\nThank for using my program! Goodbye!")

    sys.exit()  # Exit application


if __name__ == "__main__":
    print("Welcome to this directory for State data!\n")
    display_menu()
