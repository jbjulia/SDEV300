from math import pi, sin, cos, sqrt, log10

import numpy as np


def do_math():
    calc_sin()
    calc_cos()
    calc_sqrt()
    calc_log10()

    print("\nResults have been printed to text files in your current directory.")


def calc_sin():
    increment = pi / 64
    start_value = -2 * pi
    end_value = 2 * pi

    print("Generating x, sin(x) for x values ranging from -2PI -> 2PI with an increment of PI/64... Done!")

    f = open("sin.txt", mode='w', encoding='utf-8')

    for x in np.arange(start_value, end_value, increment):
        x = sin(x)
        f.write(str(x) + "\n")


def calc_cos():
    increment = pi / 64
    start_value = -2 * pi
    end_value = 2 * pi

    print("Generating x, cos(x) for x values ranging from -2PI -> 2PI with an increment of PI/64... Done!")

    f = open("cos.txt", mode='w', encoding='utf-8')

    for x in np.arange(start_value, end_value, increment):
        x = cos(x)
        f.write(str(x) + "\n")


def calc_sqrt():
    increment = 0.5
    start_value = 0
    end_value = 200

    print("Generating x, sqrt(x) for x values ranging from 0 -> 200 with an increment of 0.5... Done!")

    f = open("sqrt.txt", mode='w', encoding='utf-8')

    for x in np.arange(start_value, end_value, increment):
        x = sqrt(x)
        f.write(str(x) + "\n")


def calc_log10():
    increment = 0.5
    start_value = 0
    end_value = 200

    print("Generating x, log10(x) for x values ranging from 0 -> 200 with an increment of 0.5... Done!")

    f = open("log10.txt", mode='w', encoding='utf-8')

    for x in np.arange(start_value, end_value, increment):
        try:
            x = log10(x)
        except (ZeroDivisionError, ValueError) as e:
            f.write(str(e) + "\n")
            pass
        f.write(str(x) + "\n")


if __name__ == "__main__":
    print("Doing math - Please wait.\n")
    do_math()
