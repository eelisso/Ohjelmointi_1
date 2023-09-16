"""
Eelis Soikkeli, tehtävä 3.3
"""


def get_valid_input(data_type, prompt, allow_zero=True):
    """ Validate user input, take in datatype and input prompt as parameters """
    loop = True
    while loop:  # Create loop for input validation
        try:
            value = data_type(input(prompt).replace(",", "."))
            if allow_zero and value >= 0:
                return value  # Return input value and break loop if input is correct
            elif not allow_zero and value > 0:
                return value
            else:
                print("Invalid input.")
                continue
        except ValueError:
            print("Invalid input.")  # Print out an error and prompt the user again for correct input


def tracker():
    """ Get user input on number of tracked days and distance ran each day """
    runs = []
    days = get_valid_input(int, "Enter the number of days: ", allow_zero=False)
    for day in range(1, days + 1):
        length = get_valid_input(float, f"Enter day {day} running length: ")
        runs.append(length)  # Add each iteration to a list called "runs"
        lazy_days(runs)
    return runs


def lazy_days(runs):
    """Track amount of consecutive lazy days """
    threshold = 0  # Set threshold for "lazy days"
    count = 0  # Tracker for amount of consecutive "lazy days"
    for length in runs:
        if length <= threshold:
            count += 1
            if count >= 3:
                raise Exception("\nYou had too many consecutive lazy days!")
        else:
            count = 0


def mean_calc(runs):
    """ Calculate the mean of distance ran """
    mean = sum(runs) / len(runs)
    if mean < 3:
        print(f"\nYour running mean of {mean:.2f} km was too low!")
    else:
        print(f"\nYou were persistent runner! With a mean of {mean:.2f} km.")


def main():
    try:
        runs_list = tracker()
        mean_calc(runs_list)
    except Exception as e:
        print(e)


main()
