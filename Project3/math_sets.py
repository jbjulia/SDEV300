import logging
import sys


class Style:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def display_menu():
    menu = {
        1: "\tDisplay the Square and Cube for Integers ranging from 1 to 100",
        2: "\tSearch the sets for a specific Integer and display the Square and Cube values",
        3: "\tDisplay the Union of Square and Cube sets",
        4: "\tDisplay the Intersection of Square and Cube sets",
        5: "\tDisplay the Difference of Square and Cube sets",
        6: "\tQuit (Exit application)"
    }

    options = menu.keys()

    for item in options:
        if item == 6:
            print("\t", Style.RED + str(item), menu[item] + Style.END)  # Change item six to RED font
        else:
            print("\t", Style.BOLD + str(item) + Style.END, menu[item])  # Print selection menu with BOLD numbers

    try:
        selection = int(input("\nPlease select an option from the menu above: " + Style.GREEN + Style.END))

        if selection == 1:
            square_cubed_sets()
        elif selection == 2:
            integer = 0
            try:
                integer = int(input("\nPlease enter an integer: "))
            except ValueError:
                print("\nPlease enter a valid integer.")
                display_menu()
            square_cubed_sets(integer)
        elif selection == 3:
            find_union()
        elif selection == 4:
            find_intersection()
        elif selection == 5:
            find_difference()
        elif selection == 6:
            print("\nGoodbye!")
            sys.exit()
        else:
            print("\nPlease try again.")
    except ValueError:
        print("\nPlease make a selection by typing either '1', '2', '3', '4', '5' or '6'")
    except Exception as e:
        print("\nAn error occurred and has been logged.")
        logging.exception(e)


def square_cubed_sets(integer=None):
    integers_set = set(i for i in range(1, 101))  # Create and initialize set for integers 1 through 100
    squared_set = set()
    cubed_set = set()

    try:
        if integer is not None:  # Check if integer variable was passed
            squared_int = integer * integer  # Calculate squared values
            cubed_int = squared_int * integer  # Calculate cubed values

            print(
                "\n",
                Style.BOLD + "\tInt:\t\t" + str(integer) + "\n" + Style.END,
                Style.CYAN + "\tSquared:\t" + str(squared_int) + "\n" + Style.END,
                Style.YELLOW + "\tCubed:\t\t" + str(cubed_int) + "\n" + Style.END
            )
        else:
            for integer in integers_set:
                squared_int = integer * integer  # Calculate squared values
                squared_set.add(squared_int)  # Add squared integer to set

                cubed_int = squared_int * integer  # Calculate cubed values
                cubed_set.add(cubed_int)  # Add cubed integer to set

                print(
                    Style.BOLD + "\t" + str(integer) + "\t" + Style.END,
                    Style.CYAN + "\t" + str(squared_int) + "\t" + Style.END,
                    Style.YELLOW + "\t" + str(cubed_int) + "\t" + Style.END
                )
    except ArithmeticError:
        print("\nAn error has occurred -- Please try again")
        display_menu()  # Return to selection menu
    finally:
        print(
            "\t--------------------------\n",
            Style.BOLD + "\t" + "Int" + "\t" + Style.END,
            Style.CYAN + "\t" + "Squared" + "\t" + Style.END,
            Style.YELLOW + "\t" + "Cubed" + "\t" + Style.END
        )  # Print legend

    return [squared_set, cubed_set]  # Return both squared and cubed integer sets inside of a list


def find_union():
    union_set = set().union(square_cubed_sets()[0], square_cubed_sets()[1])  # Find the union3

    print(
        "\n",
        Style.BOLD + Style.UNDERLINE + "Union Set (Squared Ints, Cubed Ints):\n" + Style.END,
        union_set,
        "\n"
    )

    display_menu()  # Return to selection menu


def find_intersection():
    intersection_set = set(square_cubed_sets()[0].intersection(square_cubed_sets()[1]))  # Find the intersection

    print(
        "\n",
        Style.BOLD + Style.UNDERLINE + "Intersection Set (Squared Ints, Cubed Ints):\n" + Style.END,
        intersection_set,
        "\n"
    )

    display_menu()  # Return to selection menu


def find_difference():
    difference_set = set(square_cubed_sets()[0].difference(square_cubed_sets()[1]))  # Find the difference

    print(
        "\n",
        Style.BOLD + Style.UNDERLINE + "Difference Set (Squared Ints, Cubed Ints):\n" + Style.END,
        difference_set,
        "\n"
    )

    display_menu()  # Return to selection menu


if __name__ == "__main__":
    print(Style.UNDERLINE + "Menu" + Style.END)
    display_menu()
