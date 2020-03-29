def get_user_input():
    integers_list = []  # Initialize empty list for integers

    print("Please enter your first integer: ")
    integers_list.append(int(input()))  # Gets user input and casts to int

    print("Please enter your second integer: ")
    integers_list.append(int(input()))

    print("Please enter your third integer: ")
    integers_list.append(int(input()))

    print("Please enter your fourth integer: ")
    integers_list.append(int(input()))

    print("Please enter your fifth and final integer: ")
    integers_list.append(int(input()))

    get_min_max(integers_list)  # Passes integers_list to get_min_max function

    # TODO: Error handling for non-compliant input and looping


def get_min_max(integers_list):
    min_int = min(integers_list)  # Gets min of integers_list
    max_int = max(integers_list)  # Gets max of integer_list

    print("\nThe MIN is", min_int, "and the MAX is", max_int, "\n\nGoodbye!")  # Prints both min and max integers


if __name__ == "__main__":
    print("This application will take (5) input values from the user and return the minimum and maximum values.\n\n")
    get_user_input()
