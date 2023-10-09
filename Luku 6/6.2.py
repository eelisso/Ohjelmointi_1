"""
Eelis Soikkeli, exercise 6.2
Program for tracking weather data and calculating mean and median of given data
"""


def get_valid_input(data_type, prompt, allow_zero=True, allow_negative=False):
    """ Validate user input, take datatype, input prompt, allow_zero and allow_negative as parameters """

    while True:
        try:
            value = data_type(input(prompt).replace(",", "."))  # Allow user to use both decimal separators
            if allow_zero and allow_negative:
                return value  # Return input value when zero and negative values are allowed and input is correct
            elif allow_zero and not allow_negative and value >= 0:
                return value  # Return input value when zero and negative values are not allowed, and input is correct
            elif not allow_zero and not allow_negative and value > 0:
                return value  # Return input value when zero is not allowed, and input is correct
            else:
                print("Invalid input.")
                continue
        except ValueError:
            print("Invalid input.")  # Print out an error and prompt the user again for correct input


def temperature_tracker():
    """ Track the temperature of each day in a list """

    temperature_log = []
    days = get_valid_input(int, "Enter amount of days: ", False)
    for a in range(1, days + 1):
        a = get_valid_input(float, f"Enter day {a}. temperature in Celcius: ", True, True)
        temperature_log.append(a)
    return temperature_log


def median_calc(list):
    """Calculate the median of temperatures"""

    sorted_list = sorted(list)
    middle_index = len(list) // 2  # Calculate the middle index

    if len(list) % 2 != 0:
        median = sorted_list[middle_index]  # If the list has an odd number of elements, return the middle element
    else:  # If the list has an even number of elements, return the average of the two middle elements
        middle1 = sorted_list[middle_index - 1]
        middle2 = sorted_list[middle_index]
        median = (middle1 + middle2) / 2

    print(f"Temperature median: {median:.1f}C")
    return median


def mean_calc(list):
    """ Calculate the mean of temperatures """

    mean = sum(list) / len(list)
    print(f"Temperature mean: {mean:.1f}C")
    return mean


def stat(list, median, mean):
    """ Print out statistics of the tracked data """

    above_median = False
    below_median = False

    for item in list:
        if item >= median:
            above_median = True
        elif item < median:
            below_median = True

    if above_median:
        print("Over or at median were:")
        for index, item in enumerate(list):
            if item >= median:
                print(f"Day {(index + 1):2}. {item:5.1f}C difference to mean: {(item - mean):5.1f}C")

    if below_median:
        print("Under median were:")
        for index, item in enumerate(list):
            if item < median:
                print(f"Day {(index + 1):2}. {item:5.1f}C difference to mean: {(item - mean):5.1f}C")


def main():
    log = temperature_tracker()
    mean = mean_calc(log)
    median = median_calc(log)
    stat(log, median, mean)


if __name__ == "__main__":
    main()
