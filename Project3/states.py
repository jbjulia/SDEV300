import json
import sys

import state_data


def check_json():
    try:
        open('state_data.json', 'r')  # Attempt to open json file
    except (FileNotFoundError, ValueError):
        restore_directory()  # Restore directory if file could not be opened
    finally:
        display_menu()  # Display selection menu


def display_menu():
    menu_items = [
        "[ 1 ] Display all states and their data",
        "[ 2 ] Query a specific state",
        "[ 3 ] Update state data",
        "[ 4 ] Restore directory (clear changes)",
        "[ 5 ] Quit (Exit program)"
    ]

    print("Please make a selection from the following menu:\n")

    for item in menu_items:
        print(item)  # Print selection menu

    try:
        selection = int(input("\n"))  # Get user's selection

        if selection == 1:
            display_all_state_data()
        elif selection == 2:
            query_specific_state()
        elif selection == 3:
            update_json()
        elif selection == 4:
            restore_directory()
        elif selection == 5:
            exit_program()
        else:
            print("\nSorry, please try again.\n\n")
    except ValueError:
        print("\nPlease select an option from the menu by typing either '1', '2', 3', '4' or '5'.\n\n")
        display_menu()  # Display selection menu


def display_all_state_data():
    capitol = ""
    bird = ""
    flower = ""

    with open('state_data.json', 'r') as in_file:
        data = json.load(in_file)
        try:
            for state in data["states"]:
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
        except (ImportError, KeyError):
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

    with open('state_data.json', 'r') as in_file:
        data = json.load(in_file)
        try:
            for state in data["states"]:
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
        except (ImportError, KeyError):
            print("\nError: Could not import state data.")
            sys.exit()

    if not state_found:
        print("\nSorry, that state could not be found.\n")

    input("\nPress any key to return to the selection menu...\n\n")

    display_menu()


def update_json():
    state_found = False
    capitol = ""
    bird = ""
    flower = ""
    user_input = input("\nPlease enter the name of the state you wish to update: ").lower()  # Get user input

    with open('state_data.json', 'r') as in_file:
        data = json.load(in_file)
        try:
            for state in data["states"]:
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
                                "\nPlease enter a new state capitol: ")

                            with open("state_data.json", "w") as out_file:
                                json.dump(data, out_file, indent=4, sort_keys=True)  # Write new values to json file

                            print("\nYou have successfully updated the state capitol of", key.title(), "to: ",
                                  item[0].title() + ".")
                        elif element == "bird":
                            item[1] = input(
                                "\nPlease enter a new state bird: ")

                            with open("state_data.json", "w") as out_file:
                                json.dump(data, out_file, indent=4, sort_keys=True)  # Write new values to json file

                            print("\nYou have successfully updated the state bird of", key.title(), "to: ",
                                  item[1].title() + ".")
                        elif element == "flower":
                            item[2] = input(
                                "\nPlease enter a new state flower: ")

                            with open("state_data.json", "w") as out_file:
                                json.dump(data, out_file, indent=4, sort_keys=True)  # Write new values to json file

                            print("\nYou have successfully updated the state flower of", key.title(), "to: ",
                                  item[2].title() + ".")
                        else:
                            print("\nSorry, that element does not exist, please try again.\n")
                            display_menu()
                    else:
                        pass
        except (ImportError, KeyError):
            print("\nError: Could not import state data.")
            sys.exit()

        if not state_found:
            print("\nSorry, that state could not be found.\n")

        input("\nPress any key to return to the selection menu...\n\n")

        display_menu()


def restore_directory():
    data = state_data.dir_backup  # Import backup directory from state_data.py

    try:
        with open("state_data.json", "w") as out_file:
            json.dump(data, out_file, indent=4, sort_keys=True)  # Restore default state directory
    except FileNotFoundError:
        print("Error: Unable to recover state directory.")

    print("\nState directory successfully restored!\n")

    display_menu()  # Return to selection menu


def exit_program():
    print("\nThank for using my program! Goodbye!")

    sys.exit()  # Exit application


if __name__ == "__main__":
    print("Welcome to this directory for state data!\n")
    check_json()
    display_menu()
