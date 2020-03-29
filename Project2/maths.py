from math import pi, sin, cos, sqrt, log10

import numpy as np


def do_math():
    calc_sin()
    calc_cos()
    calc_sqrt()
    calc_log10()

    print("\nResults have been printed to text files (.txt) in your current directory.\n")

    if input("Would you like to see these results in the terminal? (Y / N): ").lower() == "y":
        display_results()  # Print results to terminal
    else:
        print("\nGoodbye!")


def calc_sin():
    increment = pi / 64
    start_value = -2 * pi
    end_value = 2 * pi

    print("Generating x, sin(x) for x values ranging from -2PI -> 2PI with an increment of PI/64... Done!")

    f = open("sin.txt", mode='w', encoding='utf-8')  # Open text file, create if one does not exist

    for x in np.arange(start_value, end_value, increment):
        x = sin(x)
        f.write(str(x) + "\n")  # Write column of sin(x) values


def calc_cos():
    increment = pi / 64
    start_value = -2 * pi
    end_value = 2 * pi

    print("Generating x, cos(x) for x values ranging from -2PI -> 2PI with an increment of PI/64... Done!")

    f = open("cos.txt", mode='w', encoding='utf-8')  # Open text file, create if one does not exist

    for x in np.arange(start_value, end_value, increment):
        x = cos(x)
        f.write(str(x) + "\n")  # Write column of cos(x) values


def calc_sqrt():
    increment = 0.5
    start_value = 0
    end_value = 200

    print("Generating x, sqrt(x) for x values ranging from 0 -> 200 with an increment of 0.5... Done!")

    f = open("sqrt.txt", mode='w', encoding='utf-8')  # Open text file, create if one does not exist

    for x in np.arange(start_value, end_value, increment):
        x = sqrt(x)
        f.write(str(x) + "\n")  # Write column of sqrt(x) values


def calc_log10():
    increment = 0.5
    start_value = 0
    end_value = 200

    print("Generating x, log10(x) for x values ranging from 0 -> 200 with an increment of 0.5... Done!")

    f = open("log10.txt", mode='w', encoding='utf-8')  # Open text file, create if one does not exist

    for x in np.arange(start_value, end_value, increment):
        try:
            x = log10(x)
        except (ZeroDivisionError, ValueError) as e:
            f.write(str(e) + "\n")  # Record error message and pass
            pass
        finally:
            f.write(str(x) + "\n")  # Write column of log10(x) values


def display_results():
    x = 0
    sin_values = ""
    cos_values = ""
    sqrt_values = ""
    log10_values = ""

    try:
        sin_values = open("sin.txt", mode='r', encoding='utf-8')  # Open text files and read in data
        cos_values = open("cos.txt", mode='r', encoding='utf-8')
        sqrt_values = open("sqrt.txt", mode='r', encoding='utf-8')
        log10_values = open("log10.txt", mode='r', encoding='utf-8')
    except (FileNotFoundError, ImportError):
        x = x + 1  # Record number of errors encountered
        pass
    finally:
        print("\nSin(x) Values:\n",
              sin_values.read(),  # Print values to terminal
              "\nCos(x) Values:\n",
              cos_values.read(),
              "\nSqrt(x) Values:\n",
              sqrt_values.read(),
              "\nLog10(x) Values:\n",
              log10_values.read(),
              "\nGoodbye!")

    if x > 0:
        print("\nError: ", x, "file(s) could not be opened.")  # Print number of errors if any occurred


if __name__ == "__main__":
    print("Doing math - Please wait.\n")
    do_math()
