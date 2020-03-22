from math import pi

import numpy as np


def do_math():
    calc_sin()
    calc_cos()
    calc_sqrt()
    # calc_log10()


def calc_sin():
    increment = pi / 64
    start_value = -2 * pi
    end_value = 2 * pi

    print("Generating sin(x) for x values ranging from -2PI -> 2PI with an increment of PI/64... Done!")

    values_list = np.sin(np.arange(start_value, end_value, increment))

    print(values_list)


def calc_cos():
    increment = pi / 64
    start_value = -2 * pi
    end_value = 2 * pi

    print("Generating cos(x) for x values ranging from -2PI -> 2PI with an increment of PI/64... Done!")

    values_list = np.cos(np.arange(start_value, end_value, increment))  # Get x values

    print(values_list)


def calc_sqrt():
    increment = 0.5
    start_value = 0
    end_value = 200

    print("Generating sqrt(x) for x values ranging from 0 -> 200 with an increment of 0.5... Done!")

    values_list = np.sqrt(np.arange(start_value, end_value, increment))  # Get x values

    print(values_list)


def calc_log10():
    increment = 0.5
    start_value = 0
    end_value = 200

    print("Generating log10(x) for x values ranging from 0 -> 200 with an increment of 0.5... Done!")

    values_list = np.log10(np.arange(start_value, end_value, increment))  # Get x values

    print(values_list)


if __name__ == "__main__":
    print("Doing math - Please wait.")
    do_math()
