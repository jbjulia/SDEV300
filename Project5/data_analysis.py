import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HOUSING = "Housing.csv"
POP_CHANGE = "PopChange.csv"


def main_menu():
    menu_items = {
        1: "Population Data",
        2: "Housing Data",
        3: "Quit (Exit application)"
    }

    for item in menu_items.keys():
        print(item, "\t", menu_items[item])  # Print selection menu

    try:
        selection = int(input("\nPlease make a selection from the menu above:\t"))  # Get user input

        if selection == 1:
            ingest_csv(POP_CHANGE)
        elif selection == 2:
            ingest_csv(HOUSING)
        elif selection == 3:
            print("\nThank you for using my program! Goodbye!")
            sys.exit()  # Exit program
    except ValueError:
        print("\nError, your selection was invalid. Please try again.\n")
        main_menu()  # Return to main menu


def ingest_csv(file):
    data_frame = pd.read_csv(file)  # Read in csv file

    if file == POP_CHANGE:
        PopChange(data_frame)
    else:
        Housing(data_frame)


def generate_histogram(data):
    np.random.seed(214801)

    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    n, bins, patches = plt.hist(x, 20, density=True, facecolor="b", alpha=0.75)

    plt.grid(True)
    fig1 = plt
    fig1.savefig("PopChangeHistogram.svg")

    main_menu()


class PopChange:
    def __init__(self, data_frame):
        self.data_frame = data_frame

        self.display_menu()  # Display selection menu

    def display_menu(self):
        menu_items = {
            1: "Pop Apr 1",
            2: "Pop Jul 1",
            3: "Change Pop",
            4: "Generate Histogram",
            5: "Return to Menu",
        }

        for item in menu_items.keys():
            print(item, "\t", menu_items[item])  # Print selection menu

        try:
            selection = int(input("\nSelect a column you wish to analyze:\t"))  # Get user input

            if selection == 1:
                self.analyze(self.data_frame[menu_items[1]])  # Analyze data by passing column
            elif selection == 2:
                self.analyze(self.data_frame[menu_items[2]])
            elif selection == 3:
                self.analyze(self.data_frame[menu_items[3]])
            elif selection == 4:
                generate_histogram(self.data_frame)
            elif selection == 5:
                main_menu()  # Return to main menu
        except ValueError:
            print("\nError, your selection was invalid. Please try again.\n")
            self.display_menu()  # Return to selection menu

    def analyze(self, data):
        pop_dict = {
            "Count:": data.count(),
            "Mean:": data.mean(),
            "Std Deviation:": data.std(),
            "Min:": data.min(),
            "Max:": data.max()
        }

        for item in pop_dict.keys():
            print(item, "{:10.2F}".format(pop_dict[item]))  # Print data analysis dictionary

        self.display_menu()


class Housing:
    def __init__(self, data_frame):
        self.data_frame = data_frame

        self.display_menu()  # Display selection menu

    def display_menu(self):
        menu_items = {
            1: "Age of House",
            2: "Number of Bedrooms",
            3: "Year Built",
            4: "Number of Rooms",
            5: "Utility",
            6: "Generate Histogram",
            7: "Return to Menu",
        }

        for item in menu_items.keys():
            print(item, "\t", menu_items[item])  # Print selection menu

        try:
            selection = int(input("\nSelect a column you wish to analyze:\t"))  # Get user input

            if selection == 1:
                self.analyze(self.data_frame["AGE"])  # Analyze data by passing column
            elif selection == 2:
                self.analyze(self.data_frame["BEDRMS"])
            elif selection == 3:
                self.analyze(self.data_frame["BUILT"])
            elif selection == 4:
                self.analyze(self.data_frame["ROOMS"])
            elif selection == 5:
                self.analyze(self.data_frame["UTILITY"])
            elif selection == 6:
                generate_histogram(self.data_frame)
            elif selection == 7:
                main_menu()  # Return to main menu
        except ValueError:
            print("\nError, your selection was invalid. Please try again.\n")
            self.display_menu()  # Return to selection menu

    def analyze(self, data):
        housing_dict = {
            "Count:": data.count(),
            "Mean:": data.mean(),
            "Std Deviation:": data.std(),
            "Min:": data.min(),
            "Max:": data.max()
        }

        for item in housing_dict.keys():
            print(item, "{:10.2F}".format(housing_dict[item]))  # Print data analysis dictionary

        self.display_menu()


if __name__ == "__main__":
    print("Welcome to the my Data Analysis app!\n")
    main_menu()
