import json
import random
import re
import sys

import pandas as pd


def import_data():
    errors = False
    list_people = []

    print("\n\nTo begin, let's import our data we will be munging.")

    input("\nPress ENTER to import data...\t")

    try:
        with open("raw_data.json", "r") as in_file:
            data = json.load(in_file)

        for person in data:
            if person[0].lower() != "firstname":
                person[0] = person[0].title()  # Capitalize first name
                person[1] = person[1].title()  # Capitalize last name
                person[2] = str(generate_random_int(10))  # Assign random phone number (un-formatted)
                person[3] = str(generate_random_int(9))  # Assign random zip code (un-formatted)
                list_people.append(person)
    except (ImportError, KeyError):
        errors = True
        print("\nError loading data, please try again.")
    finally:
        if errors:
            sys.exit()
        else:
            input("\nData imported successfully!\n\nPress ENTER to wrangle data...\n")
            wrangle_data(list_people)


def wrangle_data(list_people):
    data_frame = pd.DataFrame(list_people,
                              columns=["First Name", "Last Name", "Phone Number", "Zip Code"])

    print(data_frame, "\n\nThis is our raw data.\n")

    input("\nPress ENTER to format this data frame...\n")

    data_frame["Phone Number"] = data_frame["Phone Number"].map(format_phone_number)
    data_frame["Zip Code"] = data_frame["Zip Code"].map(format_zip_code)

    print(data_frame, "\n\nThis is our formatted data.\n")

    quit_app()  # Exit application


def format_phone_number(old_phone_number):
    new_phone_number = re.fullmatch(r"(\d{3})(\d{3})(\d{4})", old_phone_number)

    return "-".join(new_phone_number.groups()) if new_phone_number else old_phone_number


def format_zip_code(old_zip_code):
    new_zip_code = re.match(r"(\d{5})", old_zip_code)

    return "".join(new_zip_code.groups()) if new_zip_code else old_zip_code


def generate_random_int(digits):
    range_start = 10 ** (digits - 1)  # Define length of random integer
    range_end = (10 ** digits) - 1

    return random.randint(range_start, range_end)  # Returns random 10/5-digit integer


def quit_app():
    print("\nThank you for using my application! Goodbye!")

    sys.exit()


if __name__ == "__main__":
    print("\nThis is an automatic data munging tool for demonstration purposes.")
    import_data()
