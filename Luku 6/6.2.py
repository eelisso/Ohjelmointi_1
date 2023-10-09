def get_valid_input(data_type, prompt, allow_zero=True, allow_negative=False):
    """ Validate user input, take in datatype and input prompt as parameters as well as if zero is allowed or not """
    while True:  # Create loop for input validation
        try:  # Create an exception handler for when the input value produces an error
            value = data_type(input(prompt).replace(",", "."))  # Allow user to use both decimal separators
            if allow_zero and allow_negative:
                return value  # Return input value when zero is allowed and input is correct
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

    temperature_log = []
    days = get_valid_input(int, "Enter amount of days: ", False)
    for a in range(1,days+1):
        a = get_valid_input(float, f"Enter day {a}. temperature in Celsius: ", True, True)
        temperature_log.append(a)
    temperature_log.sort()
    return temperature_log


def median_calc(list):
    """Calculate the median of temperatures"""

    # Calculate the middle index
    middle_index = len(list) // 2

    if len(list) % 2 != 0:
        # If the list has an odd number of elements, return the middle element,§
        median = list[middle_index]a<   
    else:
        # If the list has an even number of elements, return the average of the two middle elements
        middle1 = list[middle_index - 1]
        middle2 = list[middle_index]
        median = (middle1 + middle2) / 2

    print(f"Temperature median: {median}C")
    return median

def mean_calc(list):
    """ Calculate the mean of temperatures """
    mean = sum(list) / len(list)  # Mean equals the sum of all elements divided by the amount of elements
    print(f"Temperature mean: {mean}C")
    return mean

def stat(list, median, mean):
    for index, item in enumerate(list):
        if item > me777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777edian:
            print(f"Over or at median were: \n"
                  f"Day {index}. {item}C difference to mean: {abs(item-mean)} ")





log = temperature_tracker()
mean = mean_calc(log)
median = median_calc(log)
stat(log, median, mean)







