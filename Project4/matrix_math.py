from __future__ import print_function

import sys

import numpy as np


def display_menu():
    menu_items = {
        1: "\tAddition",
        2: "\tSubtraction",
        3: "\tMatrix Multiplication",
        4: "\tElement Multiplication",
        5: "\tStart over (Clear matrices)",
        6: "\tQuit (Exit application)"
    }

    try:
        if input("Would you like to play? [ Y / N ]\t").lower() == "y":
            matrices = build_matrices()  # Get user input to build matrices

            while matrices is not None:  # Keep returning to selection menu until user quits application
                print("\n--------------------\n")
                print("\nFirst Matrix:\n", *matrices[0], sep="\n")
                print("\nSecond Matrix:\n", *matrices[1], sep="\n")
                print("\n--------------------\n")

                for item in menu_items.keys():
                    print(item, menu_items[item])  # Print selection menu

                selection = int(input("\nPlease make a selection from the menu above: "))  # Get user input

                if selection == 1:
                    add_matrices(matrices)  # Add matrices
                elif selection == 2:
                    subtract_matrices(matrices)  # Subtract matrices
                elif selection == 3:
                    multiply_matrices(matrices)  # Multiply matrices
                elif selection == 4:
                    multiply_matrix_elements(matrices)  # Multiply matrix elements
                elif selection == 5:
                    start_over()  # Clear matrices and start over
                elif selection == 6:
                    quit_app()  # Exit application
                else:
                    print("\nUh-oh, please try again.")
        else:
            print("\nGoodbye!\n")
    except (KeyboardInterrupt, ValueError):
        print("\nError, please try again.\n")
    finally:
        sys.exit()  # Quit application


def build_matrices():
    errors = False
    matrices = [[], []]
    rows = 3  # int(input("Enter number of rows for your matrix:\t"))
    columns = 3  # int(input("Enter number of columns for your matrix:\t"))

    try:
        print("\nPlease enter your first %s x %s matrix: " % (rows, columns),
              "\n\n\t* Please use either floats or integers.",
              "\n\t* Separate your elements by hitting SPACE.",
              "\n\t* Hit ENTER to move to the next row.",
              "\n\n\tExample:\t1\t2\t3",
              "\n\t\t\t\t4\t5\t6",
              "\n\t\t\t\t7\t8\t9\n"
              )

        for i in range(rows):
            matrices[0].append(list(map(float, input().rstrip().split())))  # Build first matrix

        print("\nPlease enter your second %s x %s matrix: " % (rows, columns))

        for i in range(rows):
            matrices[1].append(list(map(float, input().rstrip().split())))  # Build second matrix
    except (KeyboardInterrupt, ValueError):
        errors = True
        pass
    finally:
        if errors:
            print("An error occurred, please try again.")

            sys.exit()  # Quit application

    np_matrix = np.array([matrices[0], matrices[1]])  # Create numpy array from matrices

    return np_matrix  # Return user's matrices


def add_matrices(matrices):
    added_matrix = np.add(matrices[0], matrices[1])

    print("\nMatrices Added:\n",
          *added_matrix,
          sep="\n"
          )  # Add matrices and pretty-print new matrix

    transpose_matrix(added_matrix)  # Find transpose of matrix
    find_mean(added_matrix)  # Find mean of matrix rows/columns


def subtract_matrices(matrices):
    subtracted_matrix = np.subtract(matrices[0], matrices[1])

    print("\nMatrices Subtracted:\n",
          *subtracted_matrix,
          sep="\n"
          )  # Subtract matrices and pretty-print new matrix

    transpose_matrix(subtracted_matrix)  # Find transpose of matrix
    find_mean(subtracted_matrix)  # Find mean of matrix rows/columns


def multiply_matrices(matrices):
    multiplied_matrix = np.matmul(matrices[0], matrices[1])

    print("\nMatrices Multiplied:\n",
          *multiplied_matrix,
          sep="\n"
          )  # Multiply matrices and pretty-print new matrix

    transpose_matrix(multiplied_matrix)  # Find transpose of matrix
    find_mean(multiplied_matrix)  # Find mean of matrix rows/columns


def multiply_matrix_elements(matrices):
    multiplied_matrix = np.multiply(matrices[0], matrices[1])

    print("\nMatrices Multiplied by Elements:\n",
          *multiplied_matrix,
          sep="\n"
          )  # Multiply matrix elements and pretty-print new matrix

    transpose_matrix(multiplied_matrix)  # Find transpose of matrix
    find_mean(multiplied_matrix)  # Find mean of matrix rows/columns


def transpose_matrix(matrix):
    matrix_transpose = np.transpose(matrix)

    print("\nMatrix Transpose:\n",
          *matrix_transpose,
          sep="\n"
          )  # Transpose added_matrix and pretty-print new matrix


def find_mean(matrix):
    row_mean = matrix.mean(axis=1)  # Calculate mean of matrix rows
    column_mean = matrix.mean(axis=0)  # Calculate mean of matrix columns

    print("\nRow Mean Values:\t",
          row_mean,
          "\nColumn Mean Values:\t",
          column_mean
          )


def start_over():
    print("\nYour matrices have been cleared!\n")

    display_menu()  # Return to selection menu


def quit_app():
    print("\nGoodbye!")

    sys.exit()  # Quit application


if __name__ == "__main__":
    print("\nWelcome to Matrix Math! Please enlarge your terminal for optimal experience.\n")
    display_menu()
