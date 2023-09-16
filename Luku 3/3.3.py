"""
Eelis Soikkeli, tehtävä 3.3
"""


def get_valid_input(data_type, prompt, allow_zero=True):
    """ Validate user input, take in datatype and input prompt as parameters as well as if zero is allowed or not """
    while True:  # Create loop for input validation
        try:  # Create an exception handler for when the input value produces an error
            value = data_type(input(prompt).replace(",", "."))  # Allow user to use both decimal separators
            if allow_zero and value >= 0:
                return value  # Return input value and break loop when zero is allowed and input is correct
            elif not allow_zero and value > 0:
                return value  # Return input value and break loop when zero is NOT allowed and input is correct
            else:
                print("Invalid input.")
                continue
        except ValueError:
            print("Invalid input.")  # Print out an error and prompt the user again for correct input


def tracker():
    """ Get user input on number of tracked days and distance ran each day """
    runs = []  # Create an empty list called runs where each days' distance ran is stored
    days = get_valid_input(int, "Enter the number of days: ",
                           allow_zero=False)  # Prompt the user for amount of days tracked
    for day in range(1, days + 1):
        length = get_valid_input(float, f"Enter day {day} running length: ")
        runs.append(length)  # Add each iteration to the "runs" -list
        lazy_days(runs)  # Run the function "lazy_days" with the "runs" -list as a parameter
    return runs  # Return the "runs" -list


def lazy_days(runs):
    """Track amount of consecutive lazy days """
    threshold = 0  # Set threshold for "lazy days"
    count = 0  # Tracker for amount of consecutive "lazy days"
    for length in runs:  # Iterate the list called "runs" and assign the values to variable called "length"
        if length <= threshold:  # 'If value of iteration is less than value of set threshold'
            count += 1  # Add 1 to the lazy day tracker
            if count >= 3:  # If tracker reaches 3 or more
                raise Exception("\nYou had too many consecutive lazy days!")  # Raise an exception
        else:  # 'If value of iteration is more than value of set threshold'
            count = 0  # Reset the tracker


def mean_calc(runs):
    """ Calculate the mean of distance ran """
    mean = sum(runs) / len(runs)  # Mean equals the sum of all elements divided by the amount of elements
    if mean < 3:
        print(f"\nYour running mean of {mean:.2f} km was too low!")  # Format the mean to 2 decimal places
    else:
        print(f"\nYou were persistent runner! With a mean of {mean:.2f} km.")


def main():
    try:  # Create a try-except block to catch the exception created earlier
        runs_list = tracker()
        mean_calc(runs_list)
    except Exception as e:
        print(e)


main()
