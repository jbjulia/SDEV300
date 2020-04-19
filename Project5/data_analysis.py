import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HOUSING = "Housing.csv"
POP_CHANGE = "PopChange.csv"


def main_menu():
    """
    Displays a selection menu inside the terminal, allowing the user to
    choose from (2) different data files (.csv) to ingest and analyze.
    :return:
    """
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
    """
    Reads in file (.csv) and pass data to the corresponding class.
    :param file:
    :return:
    """
    data_frame = pd.read_csv(file)  # Read in csv file

    if file == POP_CHANGE:
        PopChange(data_frame)
    else:
        Housing(data_frame)


def generate_histogram(data, title):
    """
    Generates a standard histogram using data passed from either class
    and saves file (.svg) to current directory.
    :param data:
    :param title:
    :return:
    """
    mu = data.mean()  # Mean of data
    sigma = data.std()  # Standard Deviation of data
    x = mu + sigma * np.random.randn(10000)

    plt.hist(x, bins='auto')
    plt.grid(True)

    plt.title(title)

    plt.savefig("{}{}".format(title, ".svg"))

    plt.show()


class PopChange:
    def __init__(self, data_frame):
        self.data_frame = data_frame

        self.display_menu()  # Display selection menu

    def display_menu(self):
        """
        Displays a selection menu inside the terminal that allows the
        user to select a column from the ingested data file to analyze.
        :return:
        """
        menu_items = {
            1: "Pop Apr 1",
            2: "Pop Jul 1",
            3: "Change Pop",
            4: "Return to Menu"
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
                main_menu()  # Return to main menu
        except ValueError:
            print("\nError, your selection was invalid. Please try again.\n")
            self.display_menu()  # Return to selection menu

    def analyze(self, data):
        """
        Creates a dictionary from the analysis conducted on the data
        passed, then prints values and prompts for optional histogram.
        :param data:
        :return:
        """
        pop_dict = {
            "\tCount:": data.count(),
            "\tMean:": data.mean(),
            "\tStd Deviation:": data.std(),
            "\tMin:": data.min(),
            "\tMax:": data.max()
        }

        print("\n", "-" * 30)

        for item in pop_dict.keys():
            print(item, "{:10.2F}".format(pop_dict[item]))  # Print data analysis dictionary

        print("-" * 30, "\n")

        try:
            if input("\nWould you like to generate a histogram? [Y / N]\t").lower() == "y":
                generate_histogram(data, "PopChangeHistogram")
                print("\nSuccess! Your histogram has been saved to this directory.\n")
        except ValueError:
            print("\nSorry, please try again.\n")
        finally:
            print("\n")
            self.display_menu()


class Housing:
    def __init__(self, data_frame):
        self.data_frame = data_frame

        self.display_menu()  # Display selection menu

    def display_menu(self):
        """
        Displays a selection menu inside the terminal that allows the
        user to select a column from the ingested data file to analyze.
        :return:
        """
        menu_items = {
            1: "Age of House",
            2: "Number of Bedrooms",
            3: "Year Built",
            4: "Number of Rooms",
            5: "Utility",
            6: "Return to Menu",
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
                main_menu()  # Return to main menu
        except ValueError:
            print("\nError, your selection was invalid. Please try again.\n")
            self.display_menu()  # Return to selection menu

    def analyze(self, data):
        """
        Creates a dictionary from the analysis conducted on the data
        passed, then prints values and prompts for optional histogram.
        :param data:
        :return:
        """
        housing_dict = {
            "\tCount:": data.count(),
            "\tMean:": data.mean(),
            "\tStd Deviation:": data.std(),
            "\tMin:": data.min(),
            "\tMax:": data.max()
        }

        print("\n", "-" * 30)

        for item in housing_dict.keys():
            print(item, "{:10.2F}".format(housing_dict[item]))  # Print data analysis dictionary

        print("-" * 30, "\n")

        try:
            if input("\nWould you like to generate a histogram? [Y / N]\t").lower() == "y":
                generate_histogram(data, "HousingHistogram")
                print("\nSuccess! Your histogram has been saved to this directory.\n")
        except ValueError:
            print("\nSorry, please try again.\n")
        finally:
            print("\n")
            self.display_menu()


if __name__ == "__main__":
    print("Welcome to the my Data Analysis app!\n")
    main_menu()
